class Clock:
    def __init__(self, hour, minute):
        self._minutes = hour * 60 + minute

    def __repr__(self):
        return f"{self.__class__.__name__}({self.get_hour()}, {self.get_minute()})"

    def __str__(self):
        # hour_string = self.get_hour()
        # minute_string = self.get_minutes()
        # include :02 to ensure there is a leading 0 if necessary
        return f"{self.get_hour():02}:{self.get_minute():02}"

    def __eq__(self, other):
        return repr(self) == repr(other)
        #return str(self) == str(other)

    def __add__(self, minutes):
        self._minutes += minutes
        return self

    def __sub__(self, minutes):
        self._minutes -= minutes
        return self

    def get_hour(self):
        return self._minutes // 60 % 24
        # return whole number of hours and make it < 24
    
    def get_minute(self):
        return self._minutes % 60
