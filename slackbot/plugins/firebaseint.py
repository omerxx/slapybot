import pyrebase


def initiate_db():
	config = {
		"apiKey": "AIzaSyD373xrqpIDXNPQ_k6IUjA9I5xGXZhM1Lc",
		"authDomain": "slackbot-93734.firebaseio.com/",
		"databaseURL": "https://slackbot-93734.firebaseio.com/",
		"storageBucket": "slackbot-93734.appspot.com",
		"serviceAccount": "/Users/omer.hamerman/projects/slackbot/slackbot/plugins/firebaseAccountCredentials.json"
	}

	firebase = pyrebase.initialize_app(config)
	auth = firebase.auth()
	return firebase.database()

