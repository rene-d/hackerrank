#! /usr/bin/env python3

# (re)construit les fichiers README.md de description des challenges

import json
import glob
import os
import io
from collections import namedtuple
import yaml

# tuple
Slug = namedtuple('Slug', ['order',         # numéro pour maintenir l'ordre
                           'link',          # lien markdown vers le fichier local
                           'track',         # lien markdown vers la sous-section du site HackerRank
                           'domain',        # lien markdown vers le domaine sur www.hackerrank.com
                           'main_track',    # identifiant du domaine (pour retrouver la description)
                           'url'])          # url vers le site web hackerrank

# globals
models = {}             # liste des challenges indexés par (contest, slug)
descriptions = {}
playlists = {}


def get_models():
    j = 0

    for i in glob.iglob(os.path.join("offline", "playlists", "*.json")):
        with open(i, "r") as f:
            data = json.load(f)
            playlists[data['slug']] = data

    for i in glob.iglob(os.path.join("offline", "contests", "*.json")):
        with open(i, "r") as f:
            data = json.load(f)

            if 'name' in data:
                desc = (data['description'] or '').partition('<br')[0]
                descriptions[data['slug']] = {'name': data['name'],
                                              'description': desc}

        for m in data['models']:
            if 'contest_slug' not in m:
                continue
            j += 1
            m['order'] = j        # ajoute un numéro pour maintenir l'ordre des chapters
            if m['contest_slug'] == 'projecteuler':
                m['order'] -= 10000         # met le ProjectEuler+ en tête des contests
            models[(m['contest_slug'], m['slug'])] = m


def do_domain(domain):

    slugs = {}

    #
    # STEP 1
    #

    for i in glob.iglob(os.path.join(domain, "**/*"), recursive=True):

        if "/js10-create-a-button/" in i:
            continue

        if os.path.isdir(i):
            # crée aussi les README.md dans chaque sous-domaine
            do_domain(i)

        if not os.path.isfile(i):
            continue

        name = os.path.basename(i)
        if name == 'CMakeLists.txt':
            continue
        if name == 'README.md':
            continue

        contest_challenge, lang = os.path.splitext(name)

        langs = {'.hs': 'Haskell',
                 '.erl': 'Erlang',
                 '.py': 'Python',
                 '.c': 'C',
                 '.cpp': 'C++',
                 '.sh': 'bash',
                 '.sql': 'SQL',
                 '.txt': 'text',
                 '.java': 'Java',
                 '.js': 'Javascript',
                 '.html': 'HTML',
                 '.pl': 'Perl'}

        lang = langs.get(lang)
        if not lang:
            # nominal: fichier à ignorer
            # print("LANG NOT FOUND:", name, os.path.splitext(name))
            continue

        contest = 'master'      # par défaut
        zz = os.path.split(os.path.dirname(i))
        if zz[0] == "contests":
            contest = zz[1]

        if (contest, contest_challenge) not in models:
            print("SLUG NOT FOUND:", name, contest_challenge, lang, i, domain)
            continue

        source = os.path.relpath(os.path.realpath(i), start=domain)

        if os.path.islink(source):
            print(source)
            exit()

        r = slugs.get((contest, contest_challenge))
        if r is None:
            m = models[(contest, contest_challenge)]
            m['onboarding'] = None

            if contest != "master":
                url = 'https://www.hackerrank.com/contests/{}/challenges/{}'.format(contest, contest_challenge)   # noqa
            else:
                url = 'https://www.hackerrank.com/challenges/{}'.format(contest_challenge)

            if zz[0] == "interview-preparation-kit":
                # print("--->", zz)
                title = "title"
                track = "track"
                main_track = "main_track"

                if zz[0] in playlists:

                    playlist = playlists[zz[0]]

                    chapter = None
                    for i, c in enumerate(playlist['playlists']):
                        if c['slug'] == zz[1]:
                            chapter = c
                            m['order'] = i + 100000000
                            break

                    title = "[{}]({})".format(
                                playlist['name'],
                                "https://www.hackerrank.com/interview/{}".format(zz[0]))

                    track = "[{}]({})".format(
                                chapter['name'],
                                "https://www.hackerrank.com/interview/{}/{}/challenges".format(zz[0], zz[1]))  # noqa

                    url = "https://www.hackerrank.com/challenges/{}/problem?h_l=playlist&slugs%5B%5D=interview&slugs%5B%5D={}&slugs%5B%5D={}".format(  # noqa
                            contest_challenge,
                            zz[0],
                            zz[1])

            elif m['track'] is not None:
                title = "[{}]({})".format(
                            m['track']['track_name'],
                            "https://www.hackerrank.com/domains/" + m['track']['track_slug'])

                track = "[{}]({}) > [{}]({})".format(
                            m['track']['track_name'],
                            "https://www.hackerrank.com/domains/" + m['track']['track_slug'],
                            m['track']['name'],
                            "https://www.hackerrank.com/domains/" +
                            m['track']['track_slug'] + "/" + m['track']['slug'])

                track = "[{}]({})".format(
                            m['track']['name'],
                            "https://www.hackerrank.com/domains/" +
                            m['track']['track_slug'] + "/" + m['track']['slug'])
                main_track = m['track']['track_slug']
            else:
                x = descriptions.get(m['contest_slug'])['name']
                title = "[{}]({})".format(x, "https://www.hackerrank.com/contests/" +
                                             m['contest_slug'])
                track = ""
                main_track = m['contest_slug']

            r = Slug(order=m['order'],
                     link=['[{}]({})'.format(lang, source)],
                     domain=title,
                     main_track=main_track,
                     track=track,
                     url=url)

            slugs[(contest, contest_challenge)] = r
        else:
            r.link.append('[{}]({})'.format(lang, source))

    order = [(v.order, contest_challenge) for contest_challenge, v in slugs.items()]
    order.sort()

    #
    # STEP 2
    #
    with io.StringIO() as out:

        if os.path.exists(os.path.join(domain, "README.md.in")):
            with open(os.path.join(domain, "README.md.in")) as f:
                out.write(f.read())

        prev_contest = None
        prev_domain = None
        prev_track = None

        for _, contest_challenge in order:

            m = models[contest_challenge]
            s = slugs[contest_challenge]

            if prev_domain != s.domain:
                prev_domain = s.domain
                print("", file=out)
                print("### " + prev_domain, file=out)
                if s.main_track in descriptions:
                    print(descriptions[s.main_track]['description'], file=out)
                print("", file=out)

            if prev_track != s.track or prev_contest != contest_challenge[0]:
                prev_contest = contest_challenge[0]
                prev_track = s.track
                if prev_track != "":
                    print("", file=out)
                    print("#### " + prev_track, file=out)
                print("", file=out)
                print("Name | Preview | Code | Difficulty", file=out)
                print("---- | ------- | ---- | ----------", file=out)

            links = ' '.join(sorted(s.link))

            preview = m['preview']
            if not preview:
                preview = m['name']
            preview = preview.replace("\n", " ").strip()

            print('[%s](%s)|%s|%s|%s' % (m['name'], s.url, preview, links,
                                         m['difficulty_name']), file=out)

        print("", file=out)

        md = out.getvalue()

    fn = os.path.join(domain, "README.md")

    if len(md.strip()) == 0:
        if os.path.exists(fn):
            print("delete", fn)
            os.unlink(fn)
    elif not os.path.exists(fn) or md != open(fn, "rt").read():
        print("rewrite", fn)
        open(fn, "wt").write(md)


def main():
    domains = yaml.load(open(os.path.join(os.path.dirname(__file__), ".hr_conf.yaml")))["domains"]

    os.chdir(os.path.dirname(__file__))
    get_models()

    for domain in domains:
        do_domain(domain)

    do_domain("coding-dojo")


if __name__ == '__main__':
    main()
