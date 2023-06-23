# syntax=docker/dockerfile:1
FROM python:3.10-alpine
ARG BOT_TOKEN
ARG CHAT_ID
# Set environment variables
ENV BOT_TOKEN=$BOT_TOKEN
ENV CHAT_ID=$CHAT_ID
# install git
RUN apk update && apk add git
# Clone git repo and install dependencies
RUN git clone https://github.com/Glhou/docker-telegram-notifier
WORKDIR /docker-telegram-notifier
RUN pip install -r requirements.txt
# Run the app
CMD ["python3", "main.py"]
