from unittest import TestCase

from tires.CarriganTire import CarriganTire
from tires.Tire import Tire


class CarriganTireTest(TestCase):

    def test_that_carrigan_tire_is_not_null(self):
        carrigan_tire: Tire = CarriganTire([0, 0, 0, 0])
        self.assertIsNotNone(carrigan_tire)

    def test_that_carrigan_tire_needs_service(self):
        carrigan_tire: Tire = CarriganTire([0.5, 0.2, 0, 0.97])
        self.assertTrue(carrigan_tire.needs_service())

    def test_that_carrigan_tire_does_not_needs_service(self):
        carrigan_tire: Tire = CarriganTire([0.89, 0, 0.4, 0.6])
        self.assertFalse(carrigan_tire.needs_service())
