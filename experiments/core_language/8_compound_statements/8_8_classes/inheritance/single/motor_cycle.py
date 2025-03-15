from vehicle import Vehicle


class MotorCycle(Vehicle):

    def __init__(self, name: str):
        self.name = name

    def wheels(self):
        return 2

    def has_roof(self):
        return False

    def usage(self):
        return """
                road trip
                racing
            """
