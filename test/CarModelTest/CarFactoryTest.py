from datetime import date
from unittest import TestCase
from car_models.CarFactory import CarFactory


class TestCarFactory(TestCase):

    def test_create_calliope_car(self):
        current_date = date(2023, 7, 23)
        last_service_date = date(2023, 6, 15)
        current_mileage = 10000
        last_service_mileage = 9000
        tire_wear = [30, 40, 20, 10]

        car = CarFactory.create_calliope_car(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)

        self.assertIsNotNone(car)
        self.assertTrue(car.needs_service())

    def test_create_glissade_car(self):
        current_date = date(2022, 7, 23)
        last_service_date = date(2020, 12, 15)
        current_mileage = 120000
        last_service_mileage = 60000
        tire_wear = [0, 5, 0, 2]

        car = CarFactory.create_glissade_car(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)

        self.assertIsNotNone(car)
        self.assertTrue(car.needs_service())

    def test_create_palindrome_car(self):
        current_date = date(2021, 7, 23)
        last_service_date = date(2021, 6, 15)
        warning_light_on = True
        tire_wear = [0.1, 0.49, 0.9, 0.5]

        car = CarFactory.create_palindrome_car(current_date, last_service_date, warning_light_on, tire_wear)

        self.assertIsNotNone(car)
        self.assertTrue(car.needs_service())

    def test_create_rorschach_car(self):
        current_date = date(2023, 7, 23)
        last_service_date = date(2020, 6, 15)
        current_mileage = 10000
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]

        car = CarFactory.create_rorschach_car(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)

        self.assertIsNotNone(car)
        self.assertFalse(car.needs_service())

    def test_create_thovex_car(self):
        current_date = date(2023, 7, 23)
        last_service_date = date(2019, 6, 15)
        current_mileage = 100000
        last_service_mileage = 9000
        tire_wear = [30, 40, 20, 10]

        car = CarFactory.create_thovex_car(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)

        self.assertIsNotNone(car)
        self.assertTrue(car.needs_service())
