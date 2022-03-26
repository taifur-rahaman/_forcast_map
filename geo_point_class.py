# Imports
from datetime import datetime
from timezonefinder import TimezoneFinder
from pytz import timezone
from sunnyday import Weather


class GeoPoint:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_time(self):
        time_zone = TimezoneFinder()
        time_zone_string = time_zone.timezone_at(lng=self.longitude, lat=self.latitude)
        if time_zone_string is None:
            return None
        else:
            return datetime.now(timezone(time_zone_string))

    def get_weather(self):
        weather = Weather(apikey="de0f24e1d209f05dd5a003b4d6cc012c", lat=self.latitude, lon=self.longitude)
        return weather.next_12h_simplified()