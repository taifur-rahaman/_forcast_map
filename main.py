# Imports
from geopy import Nominatim
from geo_point_class import GeoPoint
from folium import Map

# Getting the location name from the user
user_input = str(input("Enter the name of the Location: "))

# Using the import class to get the lat and lon of the given location
geo_location = Nominatim(user_agent="_forcast_map")
location = geo_location.geocode(user_input).raw

# Getting the latitude and the longitude
lat, lon = map(float, [location[i] for i in ["lat", "lon"]])

geo_point = GeoPoint(lat, lon)

# Folium Map
my_map = Map(location=[lat, lon])

# Saving the Map into a html file
my_map.save("map.html")

print(geo_point.get_time())
print(geo_point.get_weather())
