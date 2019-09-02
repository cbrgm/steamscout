# SteamScout

This bot can help you find and share game information. It works in any chat, just write [@steamscoutbot](https://t.me/steamscoutbot) in the text field.

## Usage

This Steam search bot automatically works in all your chats and groups, no need to add it anywhere. Simply type [@steamscoutbot](https://t.me/steamscoutbot) in any chat, then type your query (without hitting 'send'). This will open a panel with game suggestions so you can choose the right.

## Security

Add a readonly user to the database:
```
r.db('rethinkdb').table('users').insert({id: 'readonly', password: 'changeme'})
r.db('steam').table('products').grant('readonly', {read: true, write: false, config: false});
```

## Docker / Podman

```
docker run -itd --name steamscout \
	-e BOT_TOKEN=changeme \
	-e BOT_DB_HOST=rethink.cbrgm.net \
	-e BOT_DB_PORT=28015 \
	-e BOT_DB_USER=readonly \
	-e BOT_DB_PASSWORD=changeme \
	-e BOT_DB_NAME=steam \
	quay.io/cbrgm/steamscout:latest
```

## Environment Vars

* `BOT_TOKEN` : The Telegram bot token
* `BOT_DB_HOST` : The backend database host
* `BOT_DB_PORT` : The backend database port
* `BOT_DB_USER` : The database user
* `BOT_DB_PASSWORD` : The database user password
* `BOT_DB_NAME` : The database instance to be used
