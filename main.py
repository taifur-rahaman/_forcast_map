# Imports
from geopy import Nominatim

# Getting the location name from the user
user_input = str(input("Enter the name of the Location: "))

# Using the import class to get the lat and lon of the given location
geo_location = Nominatim(user_agent="_forcast_map")
location = geo_location.geocode(user_input).raw

lat = location["lat"]
lon = location["lon"]

print(lat, lon)