from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):

        if self.started == False:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        max_distance = self.fuel // self.fuel_consumption
        if distance <= max_distance:
            self.fuel -= distance * self.fuel_consumption
        else:
            raise NotEnoughFuel