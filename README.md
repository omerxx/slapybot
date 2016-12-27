[![PyPI](https://badge.fury.io/py/slackbot.svg)](https://pypi.python.org/pypi/slackbot) [![Build Status](https://secure.travis-ci.org/lins05/slackbot.svg?branch=master)](http://travis-ci.org/lins05/slackbot)

A CHAT-OPS python chat bot for [Slack](https://slack.com) based on [lins05/slackbot](https://github.com/lins05/slackbot)
Slapybot uses firebase for storing data (using [thisbejim/Pyrebase](https://github.com/thisbejim/Pyrebase))

## Features

* ChatOps ready - with deployment system, locking mechanism and more
* Weather, news, wiki, gifs and many more queries

## Installation

```
pip install -r requirements.txt
```

## Usage

### Create firebase configuration
1. Go to your firebase project url (https://console.firebase.google.com/project/<PROJECT-NAME>)
2. Overview > Project Settings > Service Accounts (tab) > GENERATE NEW PRIVATE KEY
3. Download the json file and save it in your project (Make sure to add it to .gitignore file!!!)

### Create firebase configuration
1. Create firebase.py in /plugins directory
2. 

### Generate the slack api token

First you need to get the slack api token for your bot. You have two options:

1. [Create a bot](https://my.slack.com/services/new/bot) for your team
2. If you use a real slack user, you can generate an api token on [slack web api page](https://api.slack.com/web).


### Configure the bot
1. Create a `slackbot_settings.py` and a `run.py` in your own instance of slackbot.

##### Configure the api token

Then you need to configure the `API_TOKEN` in a python module `slackbot_settings.py`, which must be located in a python import path. This will be automatically imported by the bot.

slackbot_settings.py:

```python
API_TOKEN = "<your-api-token>"
```

Alternatively, you can use the environment variable `SLACKBOT_API_TOKEN`.

##### Run the bot
```
python run.py
```
##### Configure the default answer
Add a DEFAULT_REPLY to `slackbot_settings.py`:
```python
DEFAULT_REPLY = "Sorry but I didn't understand you"
```

##### Configure the docs answer
The `message` attribute passed to [your custom plugins](#create-plugins) has an special function `message.docs_reply()` that will parse all the plugins available and return the Docs in each of them.


##### Configure the plugins
Add [your plugin modules](#create-plugins) to a `PLUGINS` list in `slackbot_settings.py`:

```python
PLUGINS = [
    'slackbot.plugins',
    'mybot.plugins',
]
```

Now you can talk to your bot in your slack client!

## Try it out:

```
@<BOT-NAME> wiki
@<BOT-NAME> random gif
@<BOT-NAME> <SOME-WORD> me
@<BOT-NAME> Whats the weather in london?
@<BOT-NAME> Get 2 news from CNN
@<BOT-NAME> Get news sources
@<BOT-NAME> deploy <SERVICE>
@<BOT-NAME> lock <SERVICE>
@<BOT-NAME> list locks
@<BOT-NAME> list services
@<BOT-NAME> add service <SERVICE-NAME>
@<BOT-NAME> unlock <SERVICE>
@<BOT-NAME> unlock all


```
