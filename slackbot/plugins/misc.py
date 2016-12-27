from slackbot.bot import respond_to, listen_to


@listen_to('take over the world')
def taking_over(message):
	message.reply('No one takes over the world without me!')



