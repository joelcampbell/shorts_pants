import config
import geocoder
import pyowm

# lookup location of current IP address
g = geocoder.ip('me')
here = g.latlng

# authenticate openweathermap API 
owm = pyowm.OWM(config.api_key)  

# retrieve temperature for location 
location = owm.weather_at_coords(*here)
w = location.get_weather()
temp = w.get_temperature('celsius')
