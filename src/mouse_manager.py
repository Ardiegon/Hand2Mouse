import mouse
from pyautogui import mouseDown, mouseUp

class MouseManager():
    def __init__(self, opt):
        self.opt = opt
        self.dragging = False
        self.scrolling = False
        self.notmoving = False

    def define_movement_type(self, events):

        if events["scroll_enable"] and not self.scrolling:
            self.scrolling = True
        elif events["scroll_disable"] and self.scrolling:
            self.scrolling = False

        if events["drag_enable"] and not self.dragging and not self.scrolling:
            mouseDown(button='left')
            self.dragging = True 
        elif events["drag_disable"] and self.dragging:
            mouseUp(button='left')
            self.dragging = False

        if events["stopmovement_enable"] and not self.notmoving:
            self.notmoving = True
        elif events["stopmovement_disable"] and self.notmoving:
            self.notmoving = False

    def move_mouse(self, move):
        if not self.notmoving and not self.scrolling:
            mouse.move(move[0], move[1], absolute=False)
        elif self.scrolling:
            mouse.wheel(-move[1]/30)
        elif self.notmoving and not self.dragging and not self.scrolling:
            return

    def click(self, events):
        if self.notmoving or self.dragging or self.scrolling:
            return
            
        if events["left_click"]:
            mouse.click("left")
        elif events["right_click"]:
            mouse.click("right")
        if events["double_click"]:
            mouse.double_click("left")
    
    def __call__(self, move, events):
        if self.opt.debug_mouse:
            print(f"Not-Moving: {self.notmoving}, Dragging: {self.dragging}, Scrolling: {self.scrolling}")
        self.define_movement_type(events)
        self.move_mouse(move)
        self.click(events)

