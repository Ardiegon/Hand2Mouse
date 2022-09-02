import mediapipe as mp

class HandDetector():
    def __init__(self):
        self.hands = mp.solutions.hands.Hands()

    def process_image(self, imageRGB):
        res_dict = {}
        success = False
        results = self.hands.process(imageRGB)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks: # working with each hand
                for id, lm in enumerate(handLms.landmark):
                    h, w, _ = imageRGB.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    res_dict[id] = (cx,cy)
            success = True
        return success, res_dict