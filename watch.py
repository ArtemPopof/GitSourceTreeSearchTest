class Watch:
    """Store and prints time in 24-hours format"""

    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def set_hours(self, hours):
        if hours > 24 or hours < 0:
            raise RuntimeError
        self.hours = hours

    def set_minutes(self, minutes):
        if minutes > 59 or minutes < 0:
            return RuntimeError
        self.minutes = minutes

    def set_seconds(self, seconds):
        if seconds > 59 or seconds < 0:
            return RuntimeError
        self.seconds = seconds

    def current_time(self):
        return "%d:%d:%d" % (self.hours, self.minutes, self.seconds)
