
from src.gesture_event import GestureEvent
from src.utilities import *

class GestureProcessor():

    def __init__(self, opt):
        self.click_threshold = opt.click_threshold
        self.cursor_sensitivity = opt.cursor_sensitivity
        self.filter_length = opt.filter_length
        self.end_counter = opt.end_counter
        self.is_opener_hand = True
        self.last_center = None


        self.gesture_events = {
            "left_click":           GestureEvent("left_click", ["index_finger"], self.filter_length),
            "right_click":          GestureEvent("right_click", ["middle_finger"], self.filter_length),
            "double_click":         GestureEvent("double_click", ["ring_finger"], self.filter_length),
            "stopmovement_enable":  GestureEvent("stopmovement_enable", ["pinkie_finger"], self.filter_length),
            "stopmovement_disable": GestureEvent("stopmovement_disable", ["pinkie_finger"], self.end_counter, reverse_counting=True),
            "drag_enable":          GestureEvent("drag_enable", ["index_finger", "middle_finger", "ring_finger", "pinkie_finger"], self.filter_length),
            "drag_disable":         GestureEvent("drag_disable", ["index_finger", "middle_finger", "ring_finger", "pinkie_finger"], self.end_counter, reverse_counting=True),
            "scroll_enable":        GestureEvent("scroll_enable", ["middle_finger", "ring_finger", "pinkie_finger"], self.filter_length),
            "scroll_disable":       GestureEvent("scroll_disable", ["middle_finger", "ring_finger", "pinkie_finger"], self.end_counter, reverse_counting=True),
            "end_program":          GestureEvent("end_program", ["turned_back"], self.end_counter)
        }


    def __call__(self, hand, reset):
        move, signals = self.raw_process(hand, reset)
        events = {}
        
        for event_id in self.gesture_events.keys():
            self.gesture_events[event_id].watch(signals)
            events[event_id] = self.gesture_events[event_id].get_output()

        return move, events


    def raw_process(self, hand, reset = False):
        
        blank_raw = ((0,0),{"index_finger":False,"middle_finger":False,"ring_finger":False,"pinkie_finger":False,"turned_back":False})
        
        if self.is_opener_hand and not reset:
            self.is_opener_hand = False
            self.last_center = calculate_center(hand)
            return blank_raw

        if reset:
            self.is_opener_hand = True
            self.last_center = None
            return blank_raw

        signals = {}
        new_center = calculate_center(hand)

        move_x = -filter_noise_movement((new_center[0] - self.last_center[0]) * self.cursor_sensitivity)
        move_y = filter_noise_movement((new_center[1] - self.last_center[1]) * self.cursor_sensitivity)
        signals["index_finger"] = calculate_squared_distance(hand, (4,8)) < self.click_threshold**2
        signals["middle_finger"] = calculate_squared_distance(hand, (4,12)) < self.click_threshold**2
        signals["ring_finger"] = calculate_squared_distance(hand, (4,16)) < self.click_threshold**2
        signals["pinkie_finger"] = calculate_squared_distance(hand, (4,20)) < self.click_threshold**2
        signals["turned_back"] = calculate_turned_back(hand)

        move = move_x, move_y

        self.last_center = new_center
        return move, signals



        

        

            



