from firebase.firebase import FirebaseApplication, FirebaseAuthentication

# fbase = firebase.FirebaseApplication('https://slackbot-93734.firebaseio.com/', None)
# authentication = firebase.FirebaseAuthentication('BHkWvJtcz3PP3e8JzoswXZAC8Yt2', 'omerxx@gmail.com')
# fbase.authentication = authentication

SECRET = 'omerhamerman'
DSN = 'https://slackbot-93734.firebaseio.com'
EMAIL = 'omerxx@gmail.com'
authentication = FirebaseAuthentication(SECRET, EMAIL, True, True)
firebase = FirebaseApplication(DSN, authentication)

print firebase.get('/services', None)
