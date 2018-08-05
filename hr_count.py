#! /usr/bin/env python3

# compte les testcases et challenges

import argparse
import os
import glob
import yaml
import pathlib
import datetime


domains = yaml.load(open(os.path.join(os.path.dirname(__file__), ".hr_conf.yaml")))["domains"]

parser = argparse.ArgumentParser(description='Count challenges')
parser.add_argument('--latest', help="check in testcases.tar.xz is up to date", action='store_true')
parser.add_argument('-m', '--missing', help="print missing testcases", action='store_true')
parser.add_argument('--copy', help="copy missing testcases", action='store_true')
parser.add_argument('-x', '--extra', help="print extra testcases", action='store_true')
parser.add_argument('--delete', help="remove extra testcases", action='store_true')
parser.add_argument('-v', '--verbose', help="verbose", action='store_true')
parser.add_argument('domain', nargs='*', help="domain", default=domains)

args = parser.parse_args()

if args.latest:
    # find the latest modification/creation into the testcases folders
    latest_t = 0
    latest_f = None
    for folder in ['testcases', 'testcases2']:
        path = os.path.join(os.path.dirname(__file__), folder)
        for f in pathlib.Path(path).glob('**/*'):
            # if f.is_dir(): continue
            st = f.lstat()
            t = max(st.st_ctime, st.st_mtime)
            # t = st.st_mtime
            if t > latest_t:
                latest_t = t
                latest_f = f

    # get the modification time for the archive
    tar_f = os.path.join(os.path.dirname(__file__), "testcases.tar.xz")
    if os.path.exists(tar_f):
        tar_t = os.lstat(tar_f).st_mtime
    else:
        tar_t = 0

    if args.verbose:
        print("{} {}".format(datetime.datetime.fromtimestamp(latest_t).ctime(), latest_f))
        print("{} {}".format(datetime.datetime.fromtimestamp(tar_t).ctime(), tar_f))

    if tar_t < latest_t:
        if args.verbose:
            print("out of date")
        exit(1)

    exit(0)


challenges = set()
challenges_with_contest = set()
solutions = set()
count = 0

for d in args.domain:
    for f in glob.iglob(os.path.join(os.path.dirname(__file__), d, "**"), recursive=True):
        if os.path.isdir(f) or not os.path.exists(f):
            continue
        filename = os.path.basename(f)

        # pas encore trouvé de solution élégante pour exclure les répertoires solution
        if "/js10-create-a-button/" in f or "/js10-buttons-container/" in f or '/js10-binary-calculator/' in f:  # noqa
            continue

        contest = os.path.relpath(f, os.path.dirname(__file__)).split(os.path.sep)
        contest = contest[1] if contest[0] == "contests" else "master"

        if filename == 'README.md' or filename == 'CMakeLists.txt':
            continue
        slug, ext = os.path.splitext(filename)
        if ext == ".hpp" or ext == ".lst":
            continue

        challenges_with_contest.add((contest, slug))
        challenges.add(slug)
        solutions.add(filename)
        count += 1

        if args.verbose:
            print(os.path.relpath(os.path.dirname(f)), slug)

        if args.missing:
            t1 = os.path.join(os.path.dirname(__file__),
                              "testcases", contest, slug + "-testcases.zip")
            t2 = os.path.join(os.path.dirname(__file__),
                              "testcases2", contest, slug + "-testcases.zip")
            if not os.path.exists(t1) and not os.path.exists(t2):
                if ext in ['.sql', '.txt']:
                    # print("no needed:", os.path.relpath(os.path.dirname(f)), slug)
                    pass
                else:
                    print("missing testcases:", os.path.relpath(os.path.dirname(f)), slug)
                    # os.system("cp -p offline/testcases/{}-testcases.zip testcases/".format(slug))

                    if args.copy:
                        os.link("offline/testcases/{}/{}-testcases.zip".format(contest, slug),
                                "testcases/{}/{}-testcases.zip".format(contest, slug))

if args.extra:
    root = os.path.join(os.path.dirname(__file__), "testcases")

    def nom(p):
        p = os.path.relpath(p, root)
        c = os.path.dirname(p)
        p = os.path.basename(p)
        assert p.find("-testcases.") > 0
        return c, p[:p.find("-testcases.")]

    t1 = os.path.join(root, "**", "*-testcases.*")
    testcases = glob.glob(t1, recursive=True)
    extras = set([nom(i) for i in testcases])
    print("nb testcases:", len(extras))
    print(*['/'.join(i) for i in set(extras) - challenges_with_contest])

    if args.delete:
        for i in testcases:
            if nom(i) not in challenges_with_contest:
                os.unlink(i)

print(len(challenges), len(challenges_with_contest), len(solutions), count)
