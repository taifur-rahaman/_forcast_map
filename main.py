# Imports
from geopy import Nominatim
from geo_point_class import GeoPoint
from folium import Map, Marker, Popup

# Getting the location name from the user
user_input = str(input("Enter the name of the Location: "))

# Using the import class to get the lat and lon of the given location
geo_location = Nominatim(user_agent="_forcast_map")
location = geo_location.geocode(user_input).raw

# Getting the latitude and the longitude
lat, lon = map(float, [location[i] for i in ["lat", "lon"]])

# Folium Map
my_map = Map(location=[lat, lon])


# Creating Geo Point
geo_point = GeoPoint(latitude=lat, longitude=lon)

# Popup Content
forcast = geo_point.get_weather()
popup_content = f"""
Time: {forcast[0][0][-8:-6]} PM, Temperature: {forcast[0][1]}F, <img src="https://openweathermap.org/img/wn/{forcast[0][3]}@2x.png" width=35px>, {forcast[0][2]}
<hr style="margin : 1px">
Time: {int(forcast[1][0][-8:-6])-12} PM, Temperature: {forcast[1][1]}F, <img src="https://openweathermap.org/img/wn/{forcast[1][3]}@2x.png" width=35px>, {forcast[1][2]}
<hr style="margin : 1px">
Time: {int(forcast[2][0][-8:-6])-12} PM, Temperature: {forcast[2][1]}F, <img src="https://openweathermap.org/img/wn/{forcast[2][3]}@2x.png" width=35px>, {forcast[2][2]}
<hr style="margin : 1px">
Time: {int(forcast[3][0][-8:-6])-12} PM, Temperature: {forcast[3][1]}F, <img src="https://openweathermap.org/img/wn/{forcast[3][3]}@2x.png" width=35px>, {forcast[3][2]}
"""

popup = Popup(popup_content, max_width=400)
popup.add_to(geo_point)
geo_point.add_to(my_map)

# Saving the Map into a html file
my_map.save("map.html")

print(geo_point.get_time())
print(geo_point.get_weather())
