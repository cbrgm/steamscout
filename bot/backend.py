#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rethinkdb import RethinkDB
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

class Database:

    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.r = RethinkDB()
        self.conn = None

    def query_results(self, query):
        """
        queries the database for games matching the given string
        """
        results = []
        if query == "":
            return results

        # query for products
        self.connect()

        cursor = self.r.table('products').filter(
                self.r.row["app_name"].match(query)
        ).limit(20).run(self.conn)

        # build result array
        for item in cursor:
            if item is not None:
                    results.append(item)

        # close the database connection 
        self.teardown()

        return results


    def connect(self):
        """
        opens a new connection to the database
        """
        try:
            # connect to the database
            self.conn = self.r.connect(
                host=self.host,
                port=self.port,
                db=self.db,
                user=self.user,
                password=self.password,
            )
        except RqlDriverError:
            abort(503, "No database connection could be established.")

    def teardown(self):
        """
        closes an open connection to the database
        """
        try:
            self.conn.close()
        except AttributeError:
            pass
