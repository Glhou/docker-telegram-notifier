# Docker telegram notifier
Telegram notification server system for my docker containers.

## Image usage

You can run the image with the following command with your telegram bot token and chat id:

```bash
docker pull ghcr.io/glhou/docker-telegram-notifier:latest
docker run -d -e BOT_TOKEN=... -e CHAT_ID=... -p 8081:8081 ghcr.io/glhou/docker-telegram-notifier:latest
```

## Installation
Just defnie the environment variable BOT_TOKEN and CHAT_ID and run the docker-compose file:
```bash
BOT_TOKEN=... CHAT_ID=... docker-compose up -d
```

You can access to these information with the api of you telegram bot

## Usage
This curl command explicit how to use the notification:
```bash
curl "http://localhost:8081/send" -d '{"service": "Test", "level": "ERROR", "message":"zsh: command not found: python"}' -H "Content-Type: application/json"
```

