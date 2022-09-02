import cv2

class CameraStream():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def __del__(self):
        self.cap.release()
        
    def getNextImage(self, rgb_result = True):
        success, image = self.cap.read()
        if not success:
            raise RuntimeError("Cannot get frame from cam")
        if rgb_result:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image
