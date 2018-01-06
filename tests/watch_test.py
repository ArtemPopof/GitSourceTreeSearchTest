from .context import watch
import unittest

class TestWatchClass(unittest.TestCase):

    def test_corrent_printing(self):
        self.assertEqual(Watch().printTime(), '0:0:0')

    def should_fails_when_invalid_minute_set(self):
        Watch().setMinutes(66)

    def should_fails_when_invalid_seconds_set(self):
        Watch().setSeconds(555)

    def should_fails_when_invalid_hours_set(self):
        Watch().setHours(24)
        Watch().setHours(26)

    def should_print_correct_time(self):
        watches = Watch()
        watches.setSeconds(50)
        watches.setMinutes(5)
        watches.setHours(20)
        self.assertEqual(watches.printTime(), '20:5:50')

        