class GestureEvent():
    def __init__(self, name, important_signals, filter_length, reverse_counting = False):
        self.name = name
        self.important_signals = important_signals
        self.filter_length = filter_length
        self.desired_signal_state = not reverse_counting
        self.counter = 0

    def watch(self, signals):
        for signal_name in self.important_signals:
            if not signals[signal_name] == self.desired_signal_state:
                self.counter = 0
                return None
        self.counter += 1

    def get_output(self):
        if self.name == "right_click":
            print(self.counter)
        return self.counter == self.filter_length

    def get_name(self):
        return self.name