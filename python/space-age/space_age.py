class SpaceAge:
    def __init__(self, seconds):
        self.earth_years = seconds / 31557600

    def on_mercury(self):
        conversion = 0.2408467 # earth years
        return round(self.earth_years/conversion, 2)

    def on_venus(self):
        conversion = 0.61519726 # earth years
        return round(self.earth_years/conversion, 2)

    def on_earth(self):
        conversion = 1
        return round(self.earth_years/conversion, 2)

    def on_mars(self):
        conversion = 1.8808158 # earth years
        return round(self.earth_years/conversion, 2)

    def on_jupiter(self):
        conversion = 11.862615 # earth years
        return round(self.earth_years/conversion, 2)

    def on_saturn(self):
        conversion = 29.447498 # earth years
        return round(self.earth_years/conversion, 2)

    def on_uranus(self):
        conversion = 84.016846 # earth years
        return round(self.earth_years/conversion, 2)

    def on_neptune(self):
        conversion = 164.79132 # earth years
        return round(self.earth_years/conversion, 2)
