#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from bot.config import Config
from bot.bot import GameScout
from bot.exceptions import BotTokenNotSetException

def preflight_checks():
    """
    Check if the required envs are set. It does not check, if the value has been set properly.
    :return:
    """
    if not os.getenv("BOT_TOKEN"):
        error = "Please set a bot token. If you do not possess one, request one from BotFather (@botfather in Telegram)."
        raise BotTokenNotSetException(error)



if __name__ == "__main__":

    # run preflight checks
    preflight_checks()

    # create a bot config
    config = Config(
        token=os.getenv("BOT_TOKEN"),
        host=os.getenv("BOT_DB_HOST"),
        port=os.getenv("BOT_DB_PORT"),
        user=os.getenv("BOT_DB_USER"),
        password=os.getenv("BOT_DB_PASSWORD"),
        db=os.getenv("BOT_DB_NAME"),
    )

    # launch GameScout bot
    gs = GameScout(config)
    gs.run()
