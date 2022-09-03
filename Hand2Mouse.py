import os
import argparse
from src import HandDetector, CameraStream, GestureProcessor
from src.mouse_manager import MouseManager

def parse_arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument("--click-threshold", type=float, default=20, help="Threshold of mouse clicks")
    parser.add_argument("--cursor-sensitivity", type=float, default=3.0, help="Factor of how movement of hand transforms into mouse movement")
    parser.add_argument("--filter-length", type=int, default=2, help="How many frames of clicking with fingers shoudl sensor read before signal")
    parser.add_argument("--end-counter", type=int, default=5, help="How many frames of turned hand should sensor read before ending")
    parser.add_argument("--debug-gestures", action="store_true", help="Show in terminal aditional info about gestures from each frame")
    parser.add_argument("--debug-mouse", action="store_true", help="Shows in terminal info about mouse controller state")
    parser.add_argument("--change-process-priority", action="store_true", help="Changes priority to above normal (TODO)") 

    args = parser.parse_args()
    
    return args

def main():
    opt = parse_arguments()
    print(opt)

    if opt.change_process_priority:
        pass #TODO
    running = True

    cs_unit = CameraStream()
    hd_unit = HandDetector()
    gp_unit = GestureProcessor(opt)
    mouse = MouseManager(opt)
   
    while running:
        image = cs_unit.getNextImage()
        success, result = hd_unit.process_image(image)
        move, gestures = gp_unit(result, not success)
        mouse(move, gestures)
        if opt.debug_gestures:
            print(gestures)
        running = not gestures["end_program"]
        

if __name__ == "__main__":
    main() 
