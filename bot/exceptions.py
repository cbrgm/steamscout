#!/usr/bin/env python
# -*- coding: utf-8 -*-

class BotTokenNotSetException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class DatabaseNotSetException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
