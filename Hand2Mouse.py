import argparse
from src import HandDetector, CameraStream, LandmarkProcessor
from src.mouse_manager import MouseManager

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--click-threshold", type=float, default=20, help="Threshold of mouse clicks")
    parser.add_argument("--cursor-sensitivity", type=float, default=2, help="Factor of how movement of hand transforms into mouse movement")
    parser.add_argument("--filter-length", type=int, default=3, help="How many frames of clicking with fingers shoudl sensor read before signal")
    parser.add_argument("--end-counter", type=int, default=10, help="How many frames of turned hand should sensor read before ending")
    args = parser.parse_args()
    return args

def main():
    opt = parse_arguments()
    running = True

    cs = CameraStream()
    hd = HandDetector()
    lp_unit = LandmarkProcessor(opt)
    mouse = MouseManager()
   
    while running:
        image = cs.getNextImage()
        success, result = hd.process_image(image)
        move, events = lp_unit(result, not success)
        mouse(move, events)
        running = not events[-1]
        

if __name__ == "__main__":
    main() 
