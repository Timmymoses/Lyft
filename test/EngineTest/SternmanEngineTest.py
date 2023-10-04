from unittest import TestCase

from engine.Engine import Engine
from engine.sternman_engine import SternmanEngine


class SternmanEngineTest(TestCase):

    def test_sternman(self):
        engine: Engine = SternmanEngine(warning_light_is_on=True)
        self.assertTrue(engine.needs_service())
