import mouse

class MouseManager():
    def __init__(self):
        self.screen_shape = None #TODO

    def move_mouse(self, move):
        mouse.move(move[0], move[1], absolute=False)

    def click(self, events):
        if events[0]:
            mouse.click("left")
        if events[1]:
            mouse.click("right")
        if events[2]:
            mouse.double_click("left")
    
    def __call__(self, move, events):
        self.move_mouse(move)
        self.click(events)

