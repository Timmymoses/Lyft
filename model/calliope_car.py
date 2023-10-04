from datetime import date

from battery.Battery import Battery
from battery.SpindlerBattery import SpindlerBattery
from car_models.Car import Car
from engine.Engine import Engine
from engine.capulet_engine import CapuletEngine


class CalliopeCar(Car):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list):
        self.battery: Battery = SpindlerBattery(last_service_date, current_date)
        self.engine: Engine = CapuletEngine(last_service_mileage, current_mileage)
        super().__init__(self.battery, self.engine, tire_wear)

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service() or self._needs_tire_service()

    def _needs_tire_service(self):
        return any(wear >= 0.9 for wear in self._tire_wear)