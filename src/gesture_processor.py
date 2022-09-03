
from src.gesture_event import GestureEvent
from src.utilities import *

class GestureProcessor():

    def __init__(self, opt):
        self.click_threshold = opt.click_threshold
        self.squared_click_threshold = self.click_threshold**2
        self.cursor_sensitivity = opt.cursor_sensitivity
        self.filter_length = opt.filter_length
        self.end_counter = opt.end_counter
        self.is_opener_hand = True
        self.last_center = None
        
        self.blank_move = (0,0)
        self.blank_signals = {"index_finger":False, "not_index_finger":True, "middle_finger":False,"not_middle_finger":True,"ring_finger":False,"pinkie_finger":False,"not_pinkie_finger":True,"left_thumb":False, "right_thumb":False, "turned_back":False}
        self.signals = {}


        self.gesture_events = {
            "left_click":           GestureEvent("left_click", ["index_finger","not_middle_finger"], self.filter_length),
            "right_click":          GestureEvent("right_click", ["middle_finger","not_index_finger"], 2*self.filter_length),
            "double_click":         GestureEvent("double_click", ["not_index_finger","not_middle_finger","ring_finger","not_pinkie_finger"], 2*self.filter_length),
            "stopmovement_enable":  GestureEvent("stopmovement_enable", ["right_thumb"], 2*self.filter_length),
            "stopmovement_disable": GestureEvent("stopmovement_disable", ["right_thumb"], self.end_counter, reverse_counting=True),
            "drag_enable":          GestureEvent("drag_enable", ["index_finger", "middle_finger", "ring_finger", "not_pinkie_finger"], self.filter_length),
            "drag_disable":         GestureEvent("drag_disable", ["middle_finger", "index_finger"], self.end_counter, reverse_counting=True),
            "scroll_enable":        GestureEvent("scroll_enable", ["not_index_finger", "not_middle_finger", "pinkie_finger"], self.filter_length),
            "scroll_disable":       GestureEvent("scroll_disable", ["ring_finger", "pinkie_finger"], self.end_counter, reverse_counting=True),
            "end_program":          GestureEvent("end_program", ["turned_back"], self.end_counter)
        }

        self.events = {x : False for x in self.gesture_events.keys()}


    def __call__(self, hand, reset):
        move, signals = self.raw_process(hand, reset)
        
        for event_id in self.gesture_events.keys():
            self.gesture_events[event_id].watch(signals)
            self.events[event_id] = self.gesture_events[event_id].get_output()

        return move, self.events


    def raw_process(self, hand, reset = False):
        
        
        
        if self.is_opener_hand and not reset:
            self.is_opener_hand = False
            self.last_center = calculate_center(hand)
            return self.blank_move, self.blank_signals

        if reset:
            self.is_opener_hand = True
            self.last_center = None
            return self.blank_move, self.blank_signals

        new_center = calculate_center(hand)

        move_x = -filter_noise_movement((new_center[0] - self.last_center[0]) * self.cursor_sensitivity)
        move_y = filter_noise_movement((new_center[1] - self.last_center[1]) * self.cursor_sensitivity)
        self.signals["index_finger"] = calculate_squared_distance(hand, (4,8)) < self.squared_click_threshold
        self.signals["not_index_finger"] = not self.signals["index_finger"]
        self.signals["middle_finger"] = calculate_squared_distance(hand, (4,12)) < self.squared_click_threshold
        self.signals["not_middle_finger"] = not self.signals["middle_finger"]
        self.signals["ring_finger"] = calculate_squared_distance(hand, (4,16)) < self.squared_click_threshold
        self.signals["not_ring_finger"] = not self.signals["ring_finger"]
        self.signals["pinkie_finger"] = calculate_squared_distance(hand, (4,20)) < self.squared_click_threshold
        self.signals["not_pinkie_finger"] = not self.signals["pinkie_finger"]
        self.signals["left_thumb"] = calculate_squared_distance(hand, (4,5)) < self.squared_click_threshold
        self.signals["right_thumb"] = calculate_squared_distance(hand, (4,13)) < self.squared_click_threshold
        self.signals["turned_back"] = calculate_turned_back(hand)

        move = move_x, move_y

        self.last_center = new_center
        return move, self.signals


