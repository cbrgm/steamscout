FROM docker.io/library/python:3.7-alpine

LABEL maintainer="Christian Bargmann <chris@cbrgm.net>" \
  org.label-schema.name="SteamScout Bot" \
  org.label-schema.vendor="Christian Bargmann" \
  org.label-schema.schema-version="1.0"

ARG VERSION

ENV BOT_TOKEN= \
    BOT_DB_HOST=localhost \
    BOT_DB_PORT=28015 \
    BOT_DB_NAME=steam \
    BOT_DB_USER=admin \
    BOT_DB_PASSWORD= \
    BOT_VERSION=$VERSION

RUN apk update \
    && apk add --no-cache build-base libffi-dev openssl-dev \
    && rm -rf /var/cache/apk/*

WORKDIR /usr/src/app

COPY . ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD python3.7 main.py
