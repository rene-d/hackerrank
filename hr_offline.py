#! /usr/bin/env python3

# télécharge les contests, domains et challenges de HackerRank
# crée une image locale permettant la résolution offline ainsi que la création des tables d'index

import json
import os
import requests
from hrinit import HackerRankParser
import argparse


def retrieve(contest, challenge, filename):
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            # print("----> ", challenge, filename)
            return f.read()

    url = "https://www.hackerrank.com/rest/contests/{}/challenges/{}".format(contest, challenge)
    r = requests.get(url)
    if r.status_code == 200:
        with open(filename, "wb") as f:
            f.write(r.content)
        return r.content


def get_path(m):
    # le modèle d'un chellenge de contest
    #   - contest   (ex: projecteuler)
    #   - slug      (ex: euler001)
    # et seront stockés avec comme aroborescence <contest>/<slug>.<extenion>

    # le modèle d'un challenge de practice
    #   - contest:  master
    #   - slug:     clé
    #   - track:    domaine/sous-domaine        (ex: algorithms/warmup)
    # et a parfois
    #   - primary_contest:      contest d'origine

    if 'track' not in m or m['track'] is None:
        path = os.path.join("models", m["contest_slug"])
    else:
        path = os.path.join("models",
                            m["contest_slug"], m["track"]["track_slug"], m["track"]["slug"])
    return path


def mirror(models, download_challenges=False):

    for m in models:

        # kind: code database
        # if m.get('kind') != 'code':
        #    print(m.get('kind'))
        #    continue

        # si manquant: video (cf. cracking the code interview)
        if 'kind' not in m:
            print(m)
            continue

        m["contest_slug"]           # master

        m["slug"]                   # solve-me-first
        m["name"]                   # Solve Me First
        m["preview"]                # This is an easy challenge ...

        if 'track' in m:
            if m['track']:
                m["track"]["track_slug"]    # algorithms
                m["track"]["track_name"]    # Algorithms
                m["track"]["slug"]          # warmup
                m["track"]["name"]          # Warmup

        if 'track' in m and m["track"]:
            print("=======> ", m["track"]["track_name"], ">", m["track"]["name"], ">", m["name"])
        else:
            print("=======> ", m["name"])

        if not download_challenges:
            continue

        path = get_path(m)

        os.makedirs(path, exist_ok=True)

        data = retrieve(m["contest_slug"], m["slug"], os.path.join(path, m["slug"] + ".json"))
        if data is None:
            print("NOT AVAILABLE")
            continue

        hr = HackerRankParser(rootdir=".")
        hr.feed(data, True)
        hr.downloads(statement=True, testcases=True)


class hackerrank:
    def __init__(self, download_challenges=False, reload_catalogs=False):
        self.download_challenges = download_challenges
        self.session = requests.Session()
        self.reload_catalogs = reload_catalogs

    def get(self, url, cache_file):
        cache_file = os.path.join('cache', cache_file)
        os.makedirs(os.path.dirname(cache_file), exist_ok=True)
        if not self.reload_catalogs and os.path.exists(cache_file):
            with open(cache_file, "rb") as f:
                return json.loads(f.read())
        else:
            print(">", url)
            r = self.session.get(url)
            if r.status_code == 200:
                with open(cache_file, "wb") as f:
                    f.write(r.content)
                return json.loads(r.content)
            else:
                print("error", r, url)

    def get_tracks(self, contest, my_caterogies=None):

        url = 'https://www.hackerrank.com/rest/contests/{}/tracks'.format(contest)
        fn = '{}_tracks.json'.format(contest)

        tracks = self.get(url, fn)

        for track in tracks['models']:
            if my_caterogies is not None and track['slug'] not in my_caterogies:
                continue
            url = 'https://www.hackerrank.com/rest/contests/{}/tracks/{}/chapters'.format(contest, track['slug'])  # noqa
            fn = '{}_{}.json'.format(contest, track['slug'])
            data = self.get(url, fn)
            chapters = data['models']

            track = {"models": [],
                     "id": track['id'],
                     "slug": track['slug'],
                     "name": track['name'],
                     "description": track['descriptions']}
            for chapter in chapters:
                data = self.get_chapter(contest, track['slug'], chapter)
                track["models"].extend(data)

            os.makedirs("contests", exist_ok=True)
            filename = os.path.join("contests", "{}_{}.json".format(contest, track['slug']))
            with open(filename, "wt") as f:
                json.dump(track, f)

            mirror(track["models"], self.download_challenges)

    def get_chapter(self, contest, track, chapter):
        slug = chapter['slug']                      # warmup
        # name = chapter['name']                      # Warmup
        count = int(chapter['challenges_count'])    # 10

        models = []
        limit = 50
        for i in range(0, count, limit):
            url = "https://www.hackerrank.com/rest/contests/{}/categories/{}%7C{}/challenges?offset={}&limit={}".format(contest, track, slug, i, limit)  # noqa
            fn = '{}_{}_{}_{:03d}.json'.format(contest, track, slug, i)
            data = self.get(url, fn)
            models.extend(data['models'])
        return models

    def get_contest(self, contest):
        url = 'https://www.hackerrank.com/rest/contests/' + contest
        fn = contest + '.json'
        data = self.get(url, fn)
        model = data['model']

        count = model['challenges_count']   # 210
        if count is None:
            return
        models = []
        limit = 50
        for offset in range(0, count, limit):
            url = "https://www.hackerrank.com/rest/contests/{}/challenges?offset={}&limit={}".format(contest, offset, limit)  # noqa
            fn = '{}_{:03d}.json'.format(contest, offset)
            data = self.get(url, fn)
            models.extend(data['models'])

        track = {"models": models,
                 "id": model['id'],
                 "slug": model['slug'],
                 "name": model['name'],
                 "description": model['description']}

        os.makedirs("contests", exist_ok=True)
        with open(os.path.join("contests", "{}.json".format(contest)), "wt") as f:
            json.dump(track, f)

        print("====>", contest)
        mirror(models, self.download_challenges)

    def all_contests(self):
        archived = self.get("https://www.hackerrank.com/rest/contests/archived?offset=0&limit=500&contest_slug=active", "contests_archived.json")  # noqa
        upcoming = self.get("https://www.hackerrank.com/rest/contests/upcoming", "contests_upcoming.json")  # noqa

        contests = set()
        for c in upcoming['models']:
            slug = c['slug']
            contests.add(slug)
            self.get_contest(slug)
        for c in archived['models']:
            slug = c['slug']
            if slug not in contests:
                contests.add(slug)
                self.get_contest(slug)

    def all_tracks(self):
        tracks = self.get("https://www.hackerrank.com/rest/contests/master/tracks", "master_tracks.json")  # noqa
        t = list(t['slug'] for t in tracks['models'])
        self.get_tracks("master", t)

    def tutorial(self, filename):
        with open(filename, "rt") as f:
            data = json.load(f)
            fn = None
            for m in data['models']:
                if 'contest_slug' in m and 'track' in m:
                    fn = os.path.join("contests", '{}_tutorials_{}.json'.format(m['contest_slug'], m['track']['slug']))  # noqa
                    break
            if fn is None:
                print("Bad file:", filename)
            if os.path.exists(fn):
                os.unlink(fn)
            os.link(filename, fn)
            mirror(data['models'], self.download_challenges)

    def interview(self):

        models = []
        stack = ['interview-preparation-kit']
        while len(stack) > 0:
            s = stack.pop()
            data = self.get('https://www.hackerrank.com/rest/playlists/{}'.format(s), 'playlist_{}.json'.format(s))  # noqa
            for playlist in data['playlists']:
                stack.append(playlist['slug'])

            if data['challenges_count'] > 0:
                d = self.get('https://www.hackerrank.com/rest/playlists/{}/challenges'.format(s), 'playlist_{}_challenges.json'.format(s))  # noqa

                print("Interview:", d['name'])
                mirror(d['challenges'], self.download_challenges)

                x = d['challenges']
                x.extend(models)
                models = x

        track = {"models": models,
                 "id": 0,
                 "slug": 'interview-preparation-kit',
                 "name": 'interview-preparation-kit',
                 "description": 'interview-preparation-kit'}

        filename = os.path.join("contests", "interview-preparation-kit.json")
        with open(filename, "wt") as f:
            json.dump(track, f)


def offline():
    parser = argparse.ArgumentParser(description='Offliner')
    parser.add_argument('--contests', help="download all contests", action='store_true')
    parser.add_argument('--tracks', help="download all tracks", action='store_true')
    parser.add_argument('-c', '--contest', help="download contest")
    parser.add_argument('-t', '--track', nargs='*', help="download a master track")
    parser.add_argument('-m', '--mirror', help="mirror challenges", action='store_true')
    parser.add_argument('-R', '--refresh', help="refresh the catalogs (do not use cache)",
                        action='store_true')
    parser.add_argument('--tutorials', help="download tutorials", action='store_true')
    parser.add_argument('--interview', help="download interview-preparation-kit",
                        action='store_true')

    args = parser.parse_args()

    x = hackerrank(args.mirror, args.refresh)

    if args.contests:
        x.all_contests()

    if args.tracks:
        x.all_tracks()

    if args.contest:
        x.get_contest(args.contest)

    if args.track:
        x.get_tracks("master", args.track)

    if args.tutorials:
        x.tutorial("tutorials/cracking-the-coding-interview.json")
        x.tutorial("tutorials/30-days-of-code.json")
        x.tutorial("tutorials/10-days-of-javascript.json")
        x.tutorial("tutorials/10-days-of-statistics.json")

    if args.interview:
        x.interview()

    if False:
        x.get_tracks("master", ["algorithms", "data-structures", "mathematics",
                                "cpp", "python", "shell", "sql", "security",
                                "fp"])
        x.get_contest("projecteuler")
        x.get_tracks("master", ["databases", "general-programming", "ai", "regex"])
        # x.get_contest("infinitum10")
        # x.get_contest("infinitum18")
        # x.get_contest("openbracket-2017")


if __name__ == '__main__':
    os.chdir(os.path.join(os.path.dirname(__file__), "offline"))
    offline()
