class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine is starting with {self.horsepower}")

class Wheel:
    def __init__(self, wheel_type):
        self.wheel_type = wheel_type

    def rotate(self):
        print(f"{self.wheel_type} wheel is rotating")

class Transmission:
    def __init__(self, trans_type):
        self.trans_type = trans_type

    def shift_gear(self):
        print(f"Transmission shifted: {self.trans_type}")

class Car:
    def __init__(self, car_engine, car_wheel, car_transmission):
        self.engine = car_engine
        self.wheel = car_wheel
        self.transmission = car_transmission

    def start(self):
        self.engine.start()
        self.wheel.rotate()
        self.transmission.shift_gear()
        print("Car is moving")
engine = Engine(150)
wheel = Wheel('Alloy')
transmission = Transmission("Automatic")
car = Car(engine, wheel, transmission)
car.start()
