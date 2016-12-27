from slackbot.bot import respond_to
import logging
from services import build_service_list
import time
from firebaseint import initiate_db

logger = logging.getLogger(__name__)

environments = ['stg', 'prod']
db = initiate_db()


def find_mutual(message, alist):
	inter = list(set(message.body['text'].split()).intersection(alist))
	return inter[0] if len(inter) > 0 else None


@respond_to('^deploy')
def deploy(message):
	services = build_service_list()
	service = find_mutual(message, services)
	locks = build_lock_list()

	if service:
		if service not in locks:
			message.reply('Deploying {}'.format(service))
		else:
			lock = db.child('locks').child(service).get().val()
			message.reply('Sorry, deployment of {} was locked by {} on *{}*'.format(service, lock['user'], lock['time']))

	else:
		message.reply('Missing params, cannot deploy {}'.format(service))


def build_lock_list():
	locklist = []
	for lock in db.child("locks").get().each():
		locklist.append(lock.key())

	return locklist


@respond_to('^lock')
def lock(message):
	services = build_service_list()
	service = find_mutual(message, services)
	locks = build_lock_list()

	if service:
		if service in locks:
			message.reply('Service {} already locked'.format(service))
		else:
			data = {'time': time.strftime("%b %d %Y %H:%M:%S"), 'user': message.get_user()}
			db.child("locks").child(service).set(data)
			message.reply('Done: *{}* is locked by {} [*{}*]'.format(service, data['user'], data['time']))
	else:
		message.reply('Could not find service to lock')


@respond_to('^unlock (.*)')
def unlock(message, options):
	services = build_service_list()
	if options == 'all':
		db.child("locks").set({'default': 'default'})
		message.reply('Done.')
		return
	service = find_mutual(message, services)
	if service:
		message.reply('Deployments of {} are now available'.format(service, message.get_user()))
		db.child("locks").child(service).remove()


@respond_to('^list locks$')
def list_locks(message):
	locks = build_lock_list()
	if len(locks) <= 1:
		message.send('There are no current locks.')
		return
	message.send('Locks are: ')
	for i, serv in enumerate(db.child("locks").get().each()):
		if serv.key() != 'default':
			message.send('{}. {} was locked by {} on {}'.format(i, serv.key(), serv.val()['user'], serv.val()['time']))


@respond_to('^list locks by (.*)')
def list_locks(message, user):
	for i, loc in enumerate(locks):
		if locks[loc].get('user', None) == user:
			message.send('{} locked deployment of {} to {}'.format(user, loc[0], loc[1]))
		else:
			logger.info(locks[loc])

