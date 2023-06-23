'''
Name: docker-telegram-notifier
Author: Louédec Glenn
Description: This python server will listen to http get requests and send a telegram message to a specific user. The bot token and the user id are stored with environment variables.
'''

import requests
import json
import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def status():
    return 'Server is running'


@app.route('/send/<string:message>')
def send(message):
    bot_token = os.environ.get('BOT_TOKEN')
    chat_id = os.environ.get('CHAT_ID')
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
    requests.get(url)
    return 'Message sent'

