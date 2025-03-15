from vehicle import Vehicle


class Sedan(Vehicle):

    def __init__(self, name: str):
        self.name = name

    def wheels(self):
        return 4

    def has_roof(self):
        return True

    def usage(self):
        return """
                commute to work
                vacation with family
                """
