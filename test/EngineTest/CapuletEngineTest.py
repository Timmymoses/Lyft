from unittest import TestCase

from engine.Engine import Engine
from engine.capulet_engine import CapuletEngine


class CapuletEngineTest(TestCase):

    def test_capulet(self):
        last_service_mileage: int = 60000
        current_mileage: int = 137000
        engine: Engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())
