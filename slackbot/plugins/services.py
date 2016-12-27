from slackbot.bot import respond_to
import logging
import pickle
import os
from firebaseint import initiate_db
import time

db = initiate_db()
print db.child("services").get().val()


logger = logging.getLogger(__name__)


def build_service_list():
	servlist = []
	for serv in db.child("services").get().each():
		servlist.append(serv.key())

	return servlist


@respond_to('^add service (.*)')
def add_service(message, service):
	services = build_service_list()
	if service in services:
		message.reply('Service {} already exists'.format(service))
	else:
		db.child("services").child(service).set(time.strftime("%d/%m/%Y"))
		message.reply('Done.')


@respond_to('^list services')
def list_services(message):
	message.send('Services are: ')
	for i, serv in enumerate(db.child("services").get().each()):
		message.send('{}. {}'.format(i+1, serv.key()))


@respond_to('^remove service (.*)')
def remove_service(message, service):
	services = build_service_list()
	if service not in services:
		message.reply('Service {} does not exist'.format(service))
	else:
		db.child("services").child(service).remove()
		message.reply('Done.')



