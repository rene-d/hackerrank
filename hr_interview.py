#! /usr/bin/env python3

# liste les sections de interview-preparation-kit
# crée les liens symboliques sur les challenges déjà réalisés par ailleurs

import os
import requests
import requests_cache
import glob
import argparse
from hrinit import Colors
import sys
import logging
import datetime
from collections import defaultdict


class Interview:
    def __init__(self):
        self.basedir = os.path.dirname(__file__)
        self.session = requests.Session()

    def get(self, playlist, content=None):
        if content:
            url = 'https://www.hackerrank.com/rest/playlists/{}/{}'.format(playlist, content)
        else:
            url = 'https://www.hackerrank.com/rest/playlists/{}'.format(playlist)
        return self.session.get(url).json()

    def run(self, create_links=False):

        # get challenges from algorithms, data-structures, tutorials
        # (interview-preparation-kit ones are picked among them)
        files = defaultdict(lambda: [])
        for i in ['algorithms', 'data-structures', 'tutorials']:
            pattern = os.path.join(self.basedir, i, "**", "*.*")
            for j in glob.iglob(pattern, recursive=True):
                if not os.path.isfile(j):
                    continue
                path, name = os.path.split(j)
                slug, lang = os.path.splitext(name)

                if name == "CMakeLists.txt" or name == "README.md" or lang == ".hpp":
                    continue
                files[slug].append(j)

        # get the playlist of playlists
        data = self.get('interview-preparation-kit')

        name = data['name']
        print("{}{}{}".format(Colors.BLUE, name, Colors.END))

        for playlist in data['playlists']:
            print("    {}{}{}".format(Colors.LIGHT_BLUE, playlist['name'], Colors.END))

            section_dir = os.path.join(self.basedir, 'interview-preparation-kit', playlist['slug'])
            os.makedirs(section_dir, exist_ok=True)

            if playlist['videos_count'] != 0:
                for video in self.get(playlist['slug'], 'videos')['videos']:
                    # Nota: duration field is in ISO-8601 duration format
                    print("        {}{:60}{} http://youtu.be/{}".format(
                        Colors.LIGHT_CYAN, video['title'], Colors.END, video['youtube_id']))

            if playlist['challenges_count'] == 0:
                print("        {}{}{}".format(Colors.LIGHT_RED, "no challenge", Colors.END))
            else:
                challenges = self.get(playlist['slug'], 'challenges')
                for challenge in challenges['challenges']:
                    print("        {}{}{}".format(Colors.GREEN, challenge['name'], Colors.END))

                    slug = challenge['slug']
                    if slug in files:
                        for i in files[slug]:
                            dest = os.path.join(section_dir, os.path.basename(i))
                            src = os.path.relpath(i, section_dir)
                            if not os.path.exists(dest):
                                print("          LINK", src)
                                if create_links:
                                    os.symlink(src, dest)


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


def set_cache(refresh=False):
    """ install the static Requests cache """
    if refresh:
        expire_after = datetime.timedelta(seconds=0)
    else:
        expire_after = datetime.timedelta(days=30)
    requests_cache.install_cache(
            cache_name=os.path.join(os.path.dirname(__file__), "cache"),
            allowable_methods=('GET', 'POST'), expire_after=expire_after)
    requests_cache.core.remove_expired_responses()


def main():
    parser = argparse.ArgumentParser(description='Offliner for Interview Preparation Kit')
    parser.add_argument("-v", "--verbose", help="increase verbosity", action='store_true')
    parser.add_argument('-R', '--refresh', help="refresh the catalogs (do not use cache)", action="store_true")  # noqa
    parser.add_argument('-l', '--links', help="create symlinks", action='store_true')

    args = parser.parse_args()

    set_logging(args.verbose)
    set_cache(args.refresh)

    interview = Interview()
    interview.run(args.links)


if __name__ == '__main__':
    main()
