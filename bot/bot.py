#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import itertools as it
from bot import helper
from bot.backend import Database
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

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

        self.templates = helper.load_templates()
        self.add_commands()

    def add_commands(self):
        """
        Add commands to the dispatcher
        :return:
        """
        self.dp.add_handler(CommandHandler("start", self.start))
        self.dp.add_handler(CommandHandler("help", self.help))
        self.dp.add_handler(CommandHandler("imprint", self.imprint))
        self.dp.add_handler(InlineQueryHandler(self.inlinequery))

    def start(self, update, context):
        """
        Send a message when the command /start is issued.
        :param update:
        :param context:
        :return:
        """
        update.message.reply_text(
            helper.render(template=self.templates['start.html']),
            parse_mode=ParseMode.HTML,
        )

    def help(self, update, context):
        """
        Send a message when the command /help is issued.
        :param update:
        :param context:
        :return:
        """
        update.message.reply_text(
            helper.render(template=self.templates['help.html']),
            parse_mode=ParseMode.HTML,
        )

    def imprint(self, update, context):
        """
        Send a message when the command /imprint is issued.
        :param update:
        :param context:
        :return:
        """
        update.message.reply_text(
            helper.render(template=self.templates['imprint.html']),
            parse_mode=ParseMode.HTML,
        )


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

            result['tags'] = it.islice(result['tags'], 5)
            responses.append(
                InlineQueryResultArticle(

                    id=result['id'],
                    title=result['app_name'],
                    thumb_url=result['image_url'],
                    description=result['description'],
                    input_message_content=InputTextMessageContent(

                        helper.render(
                            template=self.templates['article.html'],
                            data=result,
                        ),

                        parse_mode=ParseMode.HTML,
                    ),
                 reply_markup =
                    InlineKeyboardMarkup([[InlineKeyboardButton("Show on Steam",
                                                                url=result['url'])]])
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

