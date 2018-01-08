import unittest

from watch import Watch


class TestWatchClass(unittest.TestCase):
    def test_corrent_printing(self):
        self.assertEqual(Watch().current_time(), '0:0:0')

    def should_fails_when_invalid_minute_set(self):
        self.assertRaises(Watch().set_minutes(66), RuntimeError)

    def should_fails_when_invalid_seconds_set(self):
        self.assertRaises(Watch().set_seconds(555), RuntimeError)

    def should_fails_when_invalid_hours_set(self):
        self.assertRaises(Watch().set_hours(24), RuntimeError)
        self.assertRaises(Watch().set_hours(26), RuntimeError)

    def test_print_time(self):
        watches = Watch()

        watches.set_seconds(50)
        watches.set_minutes(5)
        watches.set_hours(20)

        self.assertEqual(watches.current_time(), '20:5:50')
