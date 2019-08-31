#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

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

def load_templates():
    """
    loads all html templates from the ./bot/templates directory and stores its
    content into a dictionary. Templates will be rendered by jinja
    """
    template_dir = './bot/templates/'
    templates = {}
    files = os.listdir(template_dir)

    for template in files:
        with open(template_dir + template, 'r') as f:
            templates[template] = f.read()

    return templates
