#! /usr/bin/env python3

# liste les sections de interview-preparation-kit
# crée les liens symboliques sur les challenges déjà réalisés par ailleurs

import json
import os
import requests
import sqlite3
import glob
import argparse
from hrinit import Colors


class WwwCache:
    def __init__(self, force_refresh=False, use_cache_control=True):
        self.force_refresh = force_refresh
        self.use_cache_control = use_cache_control
        self.db = sqlite3.connect(os.path.join(os.path.dirname(__file__), ".cache.db"))
        self.db.execute('''
create table if not exists cache (
    url text not null primary key,
    data blob,
    dl_date date,
    last_modified date,
    expires date)
''')
        self.session = requests.Session()

    def get(self, url, decode_json=True):
        data = None
        headers = {}

        if self.force_refresh:
            self.db.execute("delete from cache where url=?", (url,))

        elif self.use_cache_control:
            # try to use the Last-Modified date
            cur = self.db.cursor()
            cur.execute("select data,last_modified from cache where url=?", (url,))
            # todo: verify the Expires date (or Cache-Control max-age)
            row = cur.fetchone()
            cur.close()
            if row is not None:
                data = row[0]
                headers['If-Modified-Since'] = row[1]

        else:
            # don't use the cache information
            cur = self.db.cursor()
            cur.execute("select data,last_modified from cache where url=?", (url,))
            row = cur.fetchone()
            cur.close()
            if row is not None:
                data = row[0]

        if data is None or self.use_cache_control:
            print("> {}{}{}".format(Colors.LIGHT_GREEN, url, Colors.END))
            r = self.session.get(url, headers=headers)

            print(Colors.PURPLE + repr(r) + Colors.END)
            for k, v in r.headers.items():
                print("  ", Colors.LIGHT_BLUE + k + Colors.END, v)

            if r.status_code == 304:
                # ok, the document has not been modified
                pass

            elif r.status_code == 200:
                # ideally, we should take care of Cache-Control header content
                # now, I silently ignore it, even if no-cache or max-age=0
                # and I don't manage the responses without dates but cache control headers
                def _h(name):
                    return r.headers[name] if name in r.headers else None

                cur = self.db.cursor()
                cur.execute("insert or replace into cache (url,data,dl_date,last_modified,expires) values (?,?,?,?,?)",
                            (url, r.content,
                             _h('Date'), _h('last-modified'), _h('expires')))
                cur.close()
                self.db.commit()
                data = r.content

            else:
                # error
                data = None

        if data is not None and decode_json:
            data = json.loads(data)

        return data


class Interview:
    def __init__(self, refresh_cache=False):
        self.basedir = os.path.dirname(__file__)
        self.cache = WwwCache(refresh_cache, use_cache_control=False)

    def get(self, playlist, challenge=False):
        url = 'https://www.hackerrank.com/rest/playlists/{}'.format(playlist)

        if challenge:
            url = 'https://www.hackerrank.com/rest/playlists/{}/challenges'.format(playlist)
        else:
            url = 'https://www.hackerrank.com/rest/playlists/{}'.format(playlist)

        return self.cache.get(url, decode_json=True)

    def run(self, create_links=False):

        files = {}
        for i in ['algorithms', 'data-structures', 'tutorials']:
            pattern = os.path.join(self.basedir, i, "**", "*.*")
            for j in glob.iglob(pattern, recursive=True):

                if not os.path.isfile(j):
                    continue

                path, name = os.path.split(j)
                slug, lang = os.path.splitext(name)

                if name == "CMakeLists.txt" or name == "README.md" or lang == ".hpp":
                    continue

                if slug in files:
                    files[slug].append(j)
                else:
                    files[slug] = [j]

        data = self.get('interview-preparation-kit')

        name = data['name']
        print("{}{}{}".format(Colors.BLUE, name, Colors.END))

        for playlist in data['playlists']:
            print("  {}{}{}".format(Colors.LIGHT_BLUE, playlist['name'], Colors.END))

            section_dir = os.path.join(self.basedir, 'interview-preparation-kit', playlist['slug'])
            os.makedirs(section_dir, exist_ok=True)

            challenges = self.get(playlist['slug'], True)

            if 'challenges' not in challenges:
                continue

            for challenge in challenges['challenges']:
                print("    {}{}{}".format(Colors.LIGHT_GREEN, challenge['name'], Colors.END))

                slug = challenge['slug']
                if slug in files:
                    for i in files[slug]:
                        dest = os.path.join(section_dir, os.path.basename(i))
                        src = os.path.relpath(i, section_dir)
                        if not os.path.exists(dest):
                            print("        LINK", src)
                            if create_links:
                                os.symlink(src, dest)


def main():
    parser = argparse.ArgumentParser(description='Offliner for Interview Preparation Kit')
    parser.add_argument('-R', '--refresh', help="refresh the catalogs (do not use cache)", action="store_true")  # noqa
    parser.add_argument('-l', '--links', help="create symlinks", action='store_true')

    args = parser.parse_args()

    interview = Interview(args.refresh)
    interview.run(args.links)


if __name__ == '__main__':
    main()
