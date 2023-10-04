from unittest import TestCase

from engine.Engine import Engine
from engine.willoughby_engine import WilloughbyEngine


class WilloughbyEngineTest(TestCase):

    def test_willoughby(self):
        last_service_mileage: int = 73000
        current_mileage: int = 120000
        engine: Engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())
