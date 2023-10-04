import abc
from battery.Battery import Battery
from car_models.Serviceable import Serviceable
from engine.Engine import Engine


class Car(Serviceable):

    def __init__(self, battery: Battery, engine: Engine, tire_wear: list):
        self._battery = battery
        self._engine = engine
        self._tire_wear = tire_wear

    @abc.abstractmethod
    def needs_service(self):
        pass
