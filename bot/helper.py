#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from jinja2 import Template


def render(template, **kwargs):
    """
    renders the template with passed args
    :params template:
    :params **kwargs:
    :returns string:
    """
    tmpl = Template(template)
    return tmpl.render(kwargs)


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
