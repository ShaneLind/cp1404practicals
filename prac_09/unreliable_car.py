"""
CP1404 Practical
UnreliableCar Class
"""
from car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but only drive the car
        if a random number (0-100) is below the car's reliability value"""
        if random.randint(0, 100) < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
            print(f"Drove {distance} km")
            return distance
        else:
            print(f"Drove 0 km")
            return 0
