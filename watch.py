# store and prints time in 24-hours format


class Watch:

    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def set_hours(self, hours):
        if hours > 24 or hours < 0:
            return SyntaxErrorr
        self.hours = hours

    def set_minutes(self, minutes):
        if minutes > 59 or minutes < 0:
            return SyntaxErrorr
        self.minutes = minutes

    def set_seconds(self, seconds):
        if seconds > 59 or seconds < 0:
            return SyntaxError
        self.seconds = seconds

    def print_time(self):
        print("%d:%d:%d" % (self.hours, self.minutes, self.seconds))
