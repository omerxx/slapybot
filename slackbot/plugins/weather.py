from slackbot.bot import respond_to
import requests
from firebaseint import weather_api_key

API_KEY = weather_api_key()


@respond_to('weather in (.*)')
def weather_in(message, location):
	status = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'.format(location, API_KEY)).json()
	if '200' not in str(status['cod']):
		message.send(status.get('message'))
		return
	city = status.get('name')
	weather_title = status.get('weather')[0].get('main')
	weather_desc = status.get('weather')[0].get('description')
	temp = status.get('main').get('temp')

	temp_min = status.get('main').get('temp_min')
	temp_max = status.get('main').get('temp_max')
	wind_speed = status.get('wind').get('speed')

	message.reply(u'{}: {} ({}), temprature is {} degrees celsius (ranges between {} to {})\n wind speed is {} kmh'
	              .format(city, weather_title, weather_desc, temp, temp_min, temp_max, wind_speed))


@respond_to('weather$')
def weather_where(message):
	message.reply('Weather where?')

