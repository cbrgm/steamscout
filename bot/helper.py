#!/usr/bin/env python
# -*- coding: utf-8 -*-


def format_title(item):
    """
    formats displayed title of an item displayed in the
    InlineQueryResultArticle
    :param item:
    :return string:
    """
    item_type = "Game"
    if item['is_dlc']:
        item_type = "DLC"

    return "{} • {}".format(item_type, item['app_name'])

def format_message(item):
    """
    formats the message displayed when clicking on an item displayed in the
    InlineQueryResultArticle
    :param item:
    :return string:
    """
    tags = ', '.join(tag for tag in item['tags'])
    developers = ', '.join(dev for dev in item['developers'])

    return """
*{}*
![ ]({})
_Release(d): {}_
Publisher: {}
Developers: {}

Tags: {}

{}

            """.format(item['app_name'], item['image_url'],  item['release_date'],
                       item['publisher'],item['developers'], tags,  item['description'])

