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
    json = {
            'status': 'running',
            'usage': {
                'route': '/send (POST)',
                'data' : {'service': 'String',
                          'level': 'CRITICAL,ERROR,WARNING,INFO,DEBUG,OTHER',
                          'message': 'String'}
                },
            }
    return json


@app.route('/send', methods=['POST'])
def send():
    service = request.json['service']
    level = request.json['level']
    message = request.json['message']
    m = format_message(service, level, message)
    bot_token = os.environ.get('BOT_TOKEN')
    chat_id = os.environ.get('CHAT_ID')
    if not bot_token or not chat_id:
        return 'Error: missing environment variables'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={m}'
    requests.get(url)
    return 'Message sent'

def format_message(service, level, message):
    icons = {
            'CRITICAL': '❌',
            'ERROR': '❗',
            'WARNING': '⚠️',
            'INFO': 'ℹ️',
            'DEBUG': '🐛',
            'OTHER': '🔵',
            }
    if not level in icons:
        level = 'INFO'
    return f'*{service}* - {icons[level]}{level}\n```\n{message}\n```'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
