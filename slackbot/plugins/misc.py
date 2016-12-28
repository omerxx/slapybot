from slackbot.bot import respond_to, listen_to, default_reply
import requests


@listen_to('take over the world')
def taking_over(message):
	message.reply('No one takes over the world without me!')


@respond_to('^$')
def nothing(message):
	message.reply('Talk to me')


@respond_to('^random gif')
def gif(message):
	data = {}
	while not data.get('data'):
		try:
			data = requests.get('http://api.giphy.com/v1/stickers/random?api_key=dc6zaTOxFJmzC&tag={}'.format(
				requests.get('http://randomword.setgetgo.com/get.php').text)).json()
		except Exception as e:
			print 'Bad response from giphy - {}'.format(e)
			message.send('Sorry, gif service is not available')
			return
	message.send(data['data'].get('image_original_url'))


@respond_to('^(.*) me')
def gifme(message, keyword):
	data = {}
	while not data.get('data'):
		data = requests.get('http://api.giphy.com/v1/stickers/random?api_key=dc6zaTOxFJmzC&tag={}'.format(keyword)).json()
	message.send(data['data'].get('image_original_url'))


# @respond_to('^random fact')
@respond_to('^wiki')
def wiki(message):
	title = requests.get('https://en.wikipedia.org/w/api.php?format=json&action=query&generator=random&grnnamespace=0&grnlimit=1').json()['query']['pages'].values()[0]['title']
	message.reply(u'https://en.wikipedia.org/wiki/{}'.format('_'.join(title.split())))


