from sedan import Sedan
from motor_cycle import MotorCycle
from vehicle import Vehicle

if __name__ == "__main__":
    car_name = input("Please provide car name: ")
    motor_cycle_name = input("Please provide car name: ")

    car = Sedan(car_name)
    motor_cycle = MotorCycle(motor_cycle_name)

    print(car.usage())
    print(motor_cycle.usage())
    print(car.general_usage())
    print(motor_cycle.general_usage())

    print(isinstance(car, Sedan))
    print(isinstance(car, Vehicle))
    print(isinstance(car, MotorCycle))
