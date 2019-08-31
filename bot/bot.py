#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from bot import helper
from bot.backend import Database
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.utils.helpers import escape_markdown

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


class GameScout:

    def __init__(self, config):
        # Enable logging
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)

        # init database
        self.db = Database(
            host=config.host,
            port=config.port,
            user=config.user,
            password=config.password,
            db=config.db,
        )

        # init bot
        self.logger = logging.getLogger(__name__)
        self.updater = Updater(config.token, use_context=True)
        self.dp = self.updater.dispatcher

        self.add_commands()

    def add_commands(self):
        """
        Add commands to the dispatcher
        :return:
        """
        self.dp.add_handler(CommandHandler("start", self.start))
        self.dp.add_handler(CommandHandler("help", self.help))
        self.dp.add_handler(InlineQueryHandler(self.inlinequery))

    def start(self, update, context):
        """
        Send a message when the command /start is issued.
        :param update:
        :param context:
        :return:
        """
        update.message.reply_text('Hi!')


    def help(self, update, context):
        """
        Send a message when the command /help is issued.
        :return:
        """
        update.message.reply_text('Help!')


    def inlinequery(self, update, context):
        """
        Handle the inline query.
        :param update:
        :param context:
        :return:
        """

        query = update.inline_query.query
        results = self.db.query_results(query)

        responses = [] 
        for result in results:
            responses.append(
                InlineQueryResultArticle(
                    id=result['id'],
                    title=helper.format_title(result),
                    thumb_url=result['image_url'],
                    description=result['description'],
                    input_message_content=InputTextMessageContent(
                        helper.format_message(result),
                        parse_mode=ParseMode.MARKDOWN,
                    )
                )
            )

        update.inline_query.answer(responses)


    def run(self):
        """
        run the bot
        """
        # Start the Bot
        self.updater.start_polling()
        self.updater.idle()

