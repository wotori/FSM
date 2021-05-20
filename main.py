from random import randint
from time import sleep

from fsm.asset import Lamp
from fsm.states import LightOn, LightOff
from fsm.transitions import Transition

if __name__ == '__main__':
    light = Lamp()

    light.FSM.states["on"] = LightOn()
    light.FSM.states["off"] = LightOff()

    light.FSM.transitions["to_on"] = Transition("on")
    light.FSM.transitions["to_off"] = Transition("off")

    light.FSM.set_state("on")

    for i in range(20):
        if randint(0, 2):
            if light.light_on:
                light.FSM.switch_transition("to_off")
                light.light_on = False
            else:
                light.FSM.switch_transition("to_on")
                light.light_on = True
        light.FSM.execute()
        sleep(1)
