from datetime import date

from battery.Battery import Battery
from battery.SpindlerBattery import SpindlerBattery
from car_models.Car import Car
from engine.Engine import Engine
from engine.sternman_engine import SternmanEngine


class PalindromeCar(Car):

    def __init__(self, current_date: date, last_service_date: date, warning_light_on: bool, tire_wear: list):
        self.battery: Battery = SpindlerBattery(last_service_date, current_date)
        self.sternman_engine: Engine = SternmanEngine(warning_light_on)
        super().__init__(self.battery, self.sternman_engine, tire_wear)

    def needs_service(self):
        return self.battery.needs_service() or self.sternman_engine.needs_service() or self._needs_tire_service()

    def _needs_tire_service(self):
        return any(wear >= 0.9 for wear in self._tire_wear)
