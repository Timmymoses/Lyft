from datetime import date
from unittest import TestCase
from battery.Battery import Battery
from battery.NubbinBattery import NubbinBattery


class NubbinBatteryTest(TestCase):

    def test_that_nubbin_battery_need_service(self):
        last_service: date = date(2022, 5, 19)
        current_date: date = date.today()
        battery: Battery = NubbinBattery(last_service, current_date)
        self.assertFalse(battery.needs_service())

    def test_that_nubbin_battery_deos_not_need_service(self):
        last_service: date = date(2019, 5, 19)
        current_date: date = date.today()
        battery: Battery = NubbinBattery(last_service, current_date)
        self.assertTrue(battery.needs_service())
        