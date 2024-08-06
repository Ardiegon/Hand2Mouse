from abc import ABC, abstractmethod
from platform import system

which_system = system()
if which_system == "Darwin":
    import pynput.mouse as macos_mouse_module
elif which_system == "Windows":
    import mouse as windows_mouse_module
    import pyautogui
elif which_system == "Linux":
    print("Warning! Code was not tested with Linux OS, may produce errors.")
    import mouse as windows_mouse_module
    import pyautogui

class Mouse(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def move(self, x, y, absolute = False):
        pass

    @abstractmethod
    def click(self, side):
        pass

    @abstractmethod
    def double_click(self, side):
        pass

    @abstractmethod
    def scroll(self):
        pass

class WindowsMouse(Mouse):
    def __init__(self) -> None:
        super().__init__()
        self.platform = "Windows"
    
    def move(self, x, y, absolute=False):
        windows_mouse_module.move(x, y, absolute=absolute)

    def click(self, side):
        windows_mouse_module.click(side)

    def double_click(self, side):
        windows_mouse_module.double_click(side)

    def scroll(self, val):
        windows_mouse_module.wheel(-val/30)

    def hold(self):
        pyautogui.mouseDown(button='left')

    def release(self):
        pyautogui.mouseUp(button='left')

class MacosMouse(Mouse):
    def __init__(self) -> None:
        super().__init__()
        
        self.platform = "Darwin"
        self.controller = macos_mouse_module.Controller()

    def move(self, x, y, absolute=False):
        self.controller.move(x, y)
    
    def click(self, side):
        if side == "left":
            self.controller.click(macos_mouse_module.Button.left)
        else:
            self.controller.click(macos_mouse_module.Button.right)

    def double_click(self, side):
        if side == "left":
            self.controller.click(macos_mouse_module.Button.left, 2)
        else:
            self.controller.click(macos_mouse_module.Button.right, 2)

    def scroll(self, val):
        self.controller.scroll(0, val//30)

    def hold(self):
        self.controller.press(macos_mouse_module.Button.left)

    def release(self):
        self.controller.release(macos_mouse_module.Button.left)


class MouseManager():
    def __init__(self, opt):
        self.opt = opt
        self.dragging = False
        self.scrolling = False
        self.notmoving = False
        self.platform = which_system

        if self.platform == "Darwin":
            self.mouse = MacosMouse()
        elif self.platform == "Windows":
            self.mouse = WindowsMouse()
        elif self.platform == "Linux":
            print("Warning! Code was not tested with Linux OS, may produce errors.")
            self.mouse = WindowsMouse()

    def define_movement_type(self, events):

        if events["scroll_enable"] and not self.scrolling:
            self.scrolling = True
        elif events["scroll_disable"] and self.scrolling:
            self.scrolling = False

        if events["drag_enable"] and not self.dragging and not self.scrolling:
            self.mouse.hold()
            self.dragging = True 
        elif events["drag_disable"] and self.dragging:
            self.mouse.release()
            self.dragging = False

        if events["stopmovement_enable"] and not self.notmoving:
            self.notmoving = True
        elif events["stopmovement_disable"] and self.notmoving:
            self.notmoving = False

    def move_mouse(self, move):
        if not self.notmoving and not self.scrolling:
            self.mouse.move(move[0], move[1], absolute=False)
        elif self.scrolling:
            self.mouse.scroll(move[1])
        elif self.notmoving and not self.dragging and not self.scrolling:
            return

    def click(self, events):
        if self.notmoving or self.dragging or self.scrolling:
            return
            
        if events["left_click"]:
            self.mouse.click("left")
        elif events["right_click"]:
            self.mouse.click("right")
        if events["double_click"]:
            self.mouse.double_click("left")
    
    def __call__(self, move, events):
        if self.opt.debug_mouse:
            print(f"Not-Moving: {self.notmoving}, Dragging: {self.dragging}, Scrolling: {self.scrolling}")
        self.define_movement_type(events)
        self.move_mouse(move)
        self.click(events)

