print("Built in exceptions")
try:
    raise TypeError("I broke.")
except TypeError as e:
    print(f"Encountered and error. Exception: {e}")


print("Custom exceptions")


class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg

    def handle(self):
        print("Encountered accident. Taking a detour.")


try:
    raise Accident("Red truck on top of small car")
except Accident as e:
    e.handle()
finally:
    print("Cleaning up")
