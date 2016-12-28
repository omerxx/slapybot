from firebaseint import api_ai_key
from slackbot.bot import default_reply
import apiai
import json

API_KEY = api_ai_key()


@default_reply
def default_msg(message):
	# res = requests.post('https://api.api.ai/v1/query?v=20150910')
	# message.body['text']

	ai = apiai.ApiAI(API_KEY)
	request = ai.text_request()
	request.query = message.body['text']
	response = request.getresponse().read()
	message.reply(json.loads(response)['result']['fulfillment']['speech'])
