from datetime import date
from battery.Battery import Battery
from unittest import TestCase
from battery.SpindlerBattery import SpindlerBattery


class SpindlerBatteryTest(TestCase):

    def test_spindler_battery_to_assert_for_need_service(self):
        last_service: date = date(2020, 7, 23)
        current_date: date = date.today()
        battery: Battery = SpindlerBattery(last_service, current_date)
        self.assertTrue(battery.needs_service())
