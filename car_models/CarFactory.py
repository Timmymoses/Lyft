from datetime import date
from car_models.Car import Car
from model.calliope_car import CalliopeCar
from model.glissade_car import GlissadeCar
from model.palindrome_car import PalindromeCar
from model.rorschach_car import RorschachCar
from model.thovex_car import ThovexCar


class CarFactory:

    @staticmethod
    def create_calliope_car(current_date: date, last_service_date: date, current_mileage: int,
                            last_service_mileage: int, tire_wear: list) -> Car:
        return CalliopeCar(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)

    @staticmethod
    def create_glissade_car(current_date: date, last_service_date: date, current_mileage: int,
                            last_service_mileage: int, tire_wear: list) -> Car:
        return GlissadeCar(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)

    @staticmethod
    def create_palindrome_car(current_date: date, last_service_date: date, warning_light_on: bool, tire_wear: list) -> Car:
        return PalindromeCar(current_date, last_service_date, warning_light_on, tire_wear)

    @staticmethod
    def create_rorschach_car(current_date: date, last_service_date: date, current_mileage: int,
                             last_service_mileage: int, tire_wear: list) -> Car:
        return RorschachCar(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)

    @staticmethod
    def create_thovex_car(current_date: date, last_service_date: date, current_mileage: int,
                          last_service_mileage: int, tire_wear: list) -> Car:
        return ThovexCar(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)
