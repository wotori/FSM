class FSM(object):
    def __init__(self, asset_obj):
        self.asset_obj = asset_obj
        self.states = {}
        self.transitions = {}
        self.cur_state = None
        self.transition = None

    def set_state(self, state_name):
        self.cur_state = self.states[state_name]

    def switch_transition(self, transition_name):
        self.transition = self.transitions[transition_name]

    def execute(self):
        if self.transition:
            self.transition.execute()
            self.set_state(self.transition.to_state)
            self.transition = None
        self.cur_state.execute()
