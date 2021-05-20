from .state_machine import FSM


class Lamp(object):
    def __init__(self):
        self.FSM = FSM(self)
        self.light_on = True
