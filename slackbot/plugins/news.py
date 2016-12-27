from slackbot.bot import respond_to
import requests
from firebaseint import news_api_key

API_KEY = news_api_key()


@respond_to('news from (.*)')
def news_in(message, source):
	res = requests.get('https://newsapi.org/v1/articles?source={}&apiKey={}'.format(source, API_KEY)).json()
	for word in message.body.get('text').split():
		num = 1
		if word.isdigit():
			num = int(word)
			break
	if res.get('status') == 'ok':
		for i, item in enumerate(res.get('articles')):
			if i == num:
				break
			message.send(u'*{}* ({})'.format(item.get('title'), item.get('url')))
	elif res.get('status') == 'error':
		message.send('Source does not exist or isnt available')


@respond_to('^news$')
@respond_to('news sources')
def news_sources(message):
	res = requests.get('https://newsapi.org/v1/sources').json()
	sources_str = ''
	for source in res.get('sources'):
		sources_str += '*{}*, '.format(source.get('id'))
	message.send(sources_str)
