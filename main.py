'''
Name: docker-telegram-notifier
Author: Louédec Glenn
Description: This python server will listen to http post requests and send a telegram message to a specific user. The bot token and the user id are stored with environment variables.
'''

import requests
import json
import time
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def status():
    return 'Server is running'


@app.route('/send', methods=['POST'])
def send():
    message = request.json['message']
    bot_token = os.environ.get('BOT_TOKEN')
    chat_id = os.environ.get('CHAT_ID')
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
    requests.get(url)
    return 'Message sent'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
