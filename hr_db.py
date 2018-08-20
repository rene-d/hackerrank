#! /usr/bin/env python3

import collections
import sqlite3
import glob
import json
import os
import sys
import logging


my_fields = ['id', 'slug', 'name',
             'track_id', 'track_slug', 'track_name',
             'contest_slug',
             'primary_contest_refid',
             # 'custom_case', 'is_custom', 'custom',
             'difficulty_name',
             'custom_checker_language', 'checker_program',
             'default_language', 'status'
             ]


def reorder_fields(f):
    if f in my_fields:
        return my_fields.index(f)
    return len(my_fields) + 1


class hr_db:

    def __init__(self):
        self.conn = sqlite3.connect('hackerrank.db')
        self.tables = {}
        self.inserts = {}
        self.ids = {}

    def load_models(self):
        models = []

        # load in memory models from offline tree
        logging.debug("scanning files...")
        for i in glob.iglob(os.path.join(os.path.dirname(__file__),
                                         "offline", "models",  "**", "*.json"),
                            recursive=True):
            with open(i, "rb") as f:
                data = json.load(f)
                if data['status'] is True:
                    m = data['model']
                    models.append(m)
        logging.debug("%d models found", len(models))

        # analyze models
        for m in models:
            self.analyse(m, "challenge")

        # create the database tables
        c = self.conn.cursor()
        for name, fields in self.tables.items():
            sql = "drop table if exists `{}`".format(name)
            c.execute(sql)
            sql = "create table if not exists `{}` (\n".format(name)
            sql += ",\n".join("`{}` {}".format(k, fields[k])
                              for k in sorted(fields.keys(), key=reorder_fields))
            sql += ")"
            c.execute(sql)

            sql = "insert into `{}` (\n".format(name)
            sql += ",".join("`{}`".format(k) for k in fields.keys())
            sql += ") values ("
            sql += (",?" * len(fields))[1:]
            sql += ")"
            self.inserts[name] = sql

            self.ids[name] = set()

            logging.info("table: %s %d", name, len(fields))

        c.close()
        self.conn.commit()

        # store models into the database
        logging.debug("load models")
        c = self.conn.cursor()
        for m in models:
            self.charge(c, m, "challenge")
        c.close()
        self.conn.commit()

    def charge(self, c, values, tablename):

        if values['id'] in self.ids[tablename]:
            return

        columns = []
        for k in self.tables[tablename].keys():
            if k.endswith("_refid"):
                k = k[:-6]
            v = values.get(k)
            if isinstance(v, dict):
                if "id" in v:
                    self.charge(c, v, k)
                    v = v["id"]
                else:
                    v = json.dumps(v)
            elif isinstance(v, list):
                if len(v) > 0 and not isinstance(v[0], str):
                    v = json.dumps(v)
                else:
                    try:
                        v = "|".join(v)
                    except TypeError:
                        print(k)
                        raise
            columns.append(v)
        c.execute(self.inserts[tablename], columns)
        self.ids[tablename].add(values['id'])

    def analyse(self, values, tablename):
        if tablename not in self.tables:
            logging.debug("discover table %s", tablename)
            fields = self.tables[tablename] = collections.OrderedDict()
        else:
            fields = self.tables[tablename]

        for k, v in values.items():

            if k.endswith('_template') or k.endswith('_template_head') or k.endswith('_template_tail'): continue
            if k.endswith('_skeliton_head') or k.endswith('_skeliton_tail'): continue

            if isinstance(v, str):
                t = "text"
            elif isinstance(v, bool):
                t = "boolean"
            elif isinstance(v, int):
                # enforce type for these fields
                if k in ["max_score", "factor", "success_ratio"]:
                    t = "float"
                else:
                    t = "integer"
                    if k == "id":
                        t += " primary key not null"

            elif isinstance(v, float):
                t = "float"
            elif isinstance(v, list):
                t = "text"
            elif v is None:
                continue
            elif isinstance(v, dict):
                if "id" in v:
                    t = "integer"
                    self.analyse(v, k)
                    k += "_refid"
                else:
                    t = "text"
            else:
                logging.error("unknown type: %s", type(v))

            if k in fields:
                if fields[k] != t:
                    logging.warning("mismatch {:20} type={} found={} value={} of {}".format(k, fields[k], t, repr(v), tablename))
            else:
                fields[k] = t


def set_logging(verbose):
    """ set up a colorized logger """
    if sys.stdout.isatty():
        logging.addLevelName(logging.DEBUG, "\033[0;32m%s\033[0m" % logging.getLevelName(logging.DEBUG))
        logging.addLevelName(logging.INFO, "\033[1;33m%s\033[0m" % logging.getLevelName(logging.INFO))
        logging.addLevelName(logging.WARNING, "\033[1;35m%s\033[1;0m" % logging.getLevelName(logging.WARNING))
        logging.addLevelName(logging.ERROR, "\033[1;41m%s\033[1;0m" % logging.getLevelName(logging.ERROR))

    if verbose:
        logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG, datefmt='%H:%M:%S')
    else:
        logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.ERROR, datefmt='%H:%M:%S')


if __name__ == '__main__':
    set_logging(True)
    menu = hr_db()
    menu.load_models()
