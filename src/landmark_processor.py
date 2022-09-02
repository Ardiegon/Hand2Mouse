
from signal import signal


def calculate_center(hand):
    ids = [0,5,9,13,17]
    avg_x = sum(hand[x][0] for x in ids)/len(ids)
    avg_y = sum(hand[x][1] for x in ids)/len(ids)
    return avg_x, avg_y


def calculate_squared_distance(hand, ids):
    distance_x_sq = (hand[ids[0]][0] - hand[ids[1]][0])**2
    distance_y_sq = (hand[ids[0]][0] - hand[ids[1]][0])**2
    return distance_x_sq + distance_y_sq

def calculate_turned_back(hand):
    distance_x = hand[4][0] - hand[17][0]
    return distance_x < -40
 

class LandmarkProcessor():

    def __init__(self, opt):
        self.click_threshold = opt.click_threshold
        self.cursor_sensitivity = opt.cursor_sensitivity
        self.filter_length = opt.filter_length
        self.end_counter = opt.end_counter
        self.is_opener_hand = True
        self.last_center = None

        self.signal_filter = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    def __call__(self, hand, reset):
        raw = self.raw_process(hand, reset)
        events = []
        move = (raw[0], raw[1])
        
        for signal_id in self.signal_filter.keys():
            if raw[signal_id]:
                self.signal_filter[signal_id] += 1
            else:
                self.signal_filter[signal_id] =0
            events.append(self.signal_filter[signal_id] == self.filter_length)

        return move, events


    def raw_process(self, hand, reset = False):
        blank_raw = (0,0,False,False,False,False,False)
        if self.is_opener_hand and not reset:
            self.is_opener_hand = False
            self.last_center = calculate_center(hand)
            return blank_raw

        if reset:
            self.is_opener_hand = True
            self.last_center = None
            return blank_raw

        new_center = calculate_center(hand)

        move_x = -(new_center[0] - self.last_center[0]) * self.cursor_sensitivity
        move_y = (new_center[1] - self.last_center[1]) * self.cursor_sensitivity
        index_finger = calculate_squared_distance(hand, (4,8)) < self.click_threshold**2
        middle_finger = calculate_squared_distance(hand, (4,12)) < self.click_threshold**2
        ring_finger = calculate_squared_distance(hand, (4,16)) < self.click_threshold**2
        pinkie_finger = calculate_squared_distance(hand, (4,20)) < self.click_threshold**2
        turned_back = calculate_turned_back(hand)

        self.last_center = new_center
        return int(move_x), int(move_y), index_finger, middle_finger, ring_finger, pinkie_finger, turned_back



        

        

            



