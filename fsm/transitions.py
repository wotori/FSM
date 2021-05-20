from time import sleep
from random import randint


class Transition(object):
    def __init__(self, to_state) -> object:
        self.to_state = to_state

    @staticmethod
    def execute():
        time_amount = randint(1, 3)
        print(f"Transitioning...{time_amount}")
        sleep(time_amount)
