#! /usr/bin/env python3

import collections
import sqlite3
import glob
import json
import os


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

        for i in glob.iglob(os.path.join(os.path.dirname(__file__),
                                         "offline", "models",  "**", "*.json"),
                            recursive=True):
            with open(i, "rb") as f:
                data = json.load(f)
                if data['status'] is True:
                    m = data['model']
                    models.append(m)
                    # if len(models) > 2: break

        for m in models:
            self.analyse(m, "challenge")

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

            print("table:", name, len(fields))

        c.close()
        self.conn.commit()

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
            print("discover table", tablename)
            fields = self.tables[tablename] = collections.OrderedDict()
        else:
            fields = self.tables[tablename]

        for k, v in values.items():
            t = ""

            if isinstance(v, str):
                t = "text"
            elif isinstance(v, bool):
                t = "boolean"
            elif isinstance(v, int):
                t = "integer"
                # if k == "id": t += " primary key not null"

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

            if k in fields:
                if fields[k] != t:
                    print("MISMATCH {:20} {} {}".format(k, fields[k], t))
            else:
                fields[k] = t


if __name__ == '__main__':
    menu = hr_db()
    menu.load_models()
