State = type("State", (object,), {})


class LightOn(State):

    @staticmethod
    def execute():
        print("Light is on")


class LightOff(State):

    @staticmethod
    def execute():
        print("Light is off")
