#! /usr/bin/env python3

import sys
import requests
import os
import subprocess
import json
import urllib.parse
import pprint
import argparse
import platform
import re
import email.utils
import datetime


DOMAINS = {'algorithms': 'algo',
           'mathematics': 'math',
           'data-structures': 'data'}


class HackerRankParser():

    def __init__(self, debug=False):
        self.debug = debug

        self.rootdir = os.path.dirname(__file__)

        self.model = None

        self.domain = None
        self.contest = None
        self.key = None

    def feed(self, data):
        if self.debug:
            with open("model.json", "w") as f:
                f.write(data)
            print("DEBUG: write initialData.json")
        data = json.loads(data)
        if data['status'] is True:
            self.model = data['model']

    def info(self):
        print("name    :", self.model['name'])
        print("key     :", self.model['slug'])
        if self.model['track'] is None:
            print("domain  :", self.model['primary_contest']['name'])
            print("domain  :", self.model['primary_contest']['slug'])
            self.domain = self.model['primary_contest']['slug']

        else:
            print("domain  :", self.model['track']['track_name'], ">", self.model['track']['name'])
            print("domain  :", self.model['track']['track_slug'], "/", self.model['track']['slug'])
            self.domain = self.model['track']['track_slug']

        print("preview :", self.model['preview'])

        self.contest = self.model['contest_slug']
        self.key = self.model['slug']

        if self.model['contest_slug'] == "master":
            self.link = "https://www.hackerrank.com/challenges/{}/problem".format(self.key)
        else:
            self.link = "https://www.hackerrank.com/contests/{}/challenges/{}".format(self.contest, self.key)


    def gen_stub(self, lang, overwrite=False, hpp=False):

        EXTENSIONS = {"cpp": "cpp",
                      "cpp14": "cpp",
                      "c": "c",
                      "python3": "py",
                      "haskell": "hs"}

        # auto choose the language
        if lang == "*":
            if 'languages' in self.model:
                languages = self.model['languages']
                if 'python3' in languages:
                    lang = 'python3'
                elif 'cpp14' in languages:
                    lang = 'cpp14'
                elif 'haskell' in languages:
                    lang = 'haskell'
                else:
                    print("Cannot choose a language:", ' '.join(languages))
                    return

        domain = DOMAINS.get(self.domain, self.domain)
        extension = EXTENSIONS.get(lang, lang)

        os.makedirs(os.path.join(self.rootdir, domain), exist_ok=True)

        filename = os.path.join(self.rootdir, domain, self.key + "." + extension)
        if not overwrite and os.path.exists(filename):
            print("File exists:", filename)
            return

        cmake = os.path.join(self.rootdir, domain, "CMakeLists.txt")


        def write_header(f, comment, add_skeliton=True):

            def line(text=None):
                if text is None:
                    f.write('\n')
                else:
                    f.write(comment + text + '\n')

            def skeliton(what):
                text = self.model.get(lang + "_" + what, "").strip()
                if text != "":
                    if what.find("_tail") != -1:
                        line()
                        line('(' + what + ') ' + '-' * 70)
                    f.write(text + '\n')
                    if what.find("_head") != -1:
                        line('(' + what + ') ' + '-' * 70)
                        line()
                    return True
                else:
                    return False

            line(self.model['name'])
            if 'preview' in self.model:
                line(self.model['preview'])
            line('')
            line('{}'.format(self.link))
            line('')
            line()

            if add_skeliton:
                skeliton("skeliton_head") or skeliton("template_head")
                skeliton("template")
                skeliton("skeliton_tail") or skeliton("template_tail")

        if lang == "cpp" or lang == "cpp14" or lang == "c":

            if hpp:
                filename_hpp = os.path.splitext(filename)[0] + ".hpp"

                with open(filename, "wt") as f:
                    write_header(f, '// ', add_skeliton=False)
                    f.write('\n')
                    f.write('#include "{}"\n'.format(os.path.basename(filename_hpp)))
                with open(filename_hpp, "wt") as f:
                    write_header(f, '// ', add_skeliton=True)

            else:
                with open(filename, "wt") as f:
                    write_header(f, '// ')

            with open(cmake, "at") as f:
                f.write("add_hackerrank({} {}.{})\n".format(self.key, self.key, lang[:3]))

        elif lang == "python3":
            with open(filename, "wt") as f:
                write_header(f, '# ')
            with open(cmake, "at") as f:
                f.write("add_hackerrank_py({}.py)\n".format(self.key))

        elif lang == "haskell":
            with open(filename, "wt") as f:
                write_header(f, '-- ')
            with open(cmake, "at") as f:
                f.write("#add_hackerrank_hs({}.hs)\n".format(self.key))

        else:
            print("Unknown language:", lang)
            return

        print("File created. Use « code {} » to edit it.".format(filename))
        if 'VSCODE_PID' in os.environ:
            if platform.system() == 'Windows':
                subprocess.check_call(["code.cmd", filename])
            else:
                subprocess.check_call(["code", filename])


    def download(self, overwrite=False):

        def my_parsedate(text):
            return datetime.datetime(*email.utils.parsedate(text)[:6])

        testcases_dir = os.path.join(self.rootdir, "testcases")
        statements_dir = os.path.join(self.rootdir, "statements")

        os.makedirs(testcases_dir, exist_ok=True)
        os.makedirs(statements_dir, exist_ok=True)

        testcase_file = os.path.join(testcases_dir, self.key + "-testcases.zip")
        statement_file = os.path.join(statements_dir, self.key + ".pdf")

        if overwrite or not os.path.exists(testcase_file):

            url = "https://www.hackerrank.com/rest/contests/{}/challenges/{}/download_testcases".format(self.contest, self.key)
            r = requests.get(url, allow_redirects=True)
            if r.status_code == 200:
                if r.headers['content-type'] == 'application/zip':
                    with open(testcase_file, "wb") as f:
                        f.write(r.content)

                    if r.headers.get('last-modified'):
                        d = my_parsedate(r.headers['last-modified'])
                        ts = d.timestamp()
                        os.utime(testcase_file, (ts, ts))

                    print("Testcase: {} bytes".format(len(r.content)))
            else:
                print("Testcase: download error", url, r)


        if overwrite or not os.path.exists(statement_file):

            # Last-Modified: Fri, 09 Sep 2016 09:34:28 GMT
            # Content-Disposition: inline; filename=xxx-English.pdf
            # Content-Type: application/pdf

            url = "https://www.hackerrank.com/rest/contests/{}/challenges/{}/download_pdf?language=English".format(self.contest, self.key)
            r = requests.get(url, allow_redirects=True)
            if r.status_code == 200:
                print(r.headers['content-type'])
                if r.headers['content-type'] == 'application/pdf':
                    with open(statement_file, "wb") as f:
                        f.write(r.content)

                    if r.headers.get('last-modified'):
                        d = my_parsedate(r.headers['last-modified'])
                        ts = d.timestamp()
                        os.utime(statement_file, (ts, ts))

                    print("Statement: {} bytes".format(len(r.content)))
            else:
                print("Statement: download error", url, r)


def main():

    lines = [
        "===============================================================================",
        ",--.  ,--.              ,--.                 ,------.                 ,--.     ",
        "|  '--'  | ,--,--. ,---.|  |,-. ,---. ,--.--.|  .--. ' ,--,--.,--,--, |  |,-.  ",
        "|  .--.  |' ,-.  || .--'|     /| .-. :|  .--'|  '--'.'' ,-.  ||      \\|     /  ",
        "|  |  |  |\\ '-'  |\\ `--.|  \\  \\\\   --.|  |   |  |\\  \\ \\ '-'  ||  ||  ||  \\  \\  ",
        "`--'  `--' `--`--' `---'`--'`--'`----'`--'   `--' '--' `--`--'`--''--'`--'`--' ",
        "===============================================================================",
    ]
    for i in lines:
        print(i)

    parser = argparse.ArgumentParser(description='Intialize a HackerRank challenge.')
    parser.add_argument('url', help="Challenge URL")
    parser.add_argument('-v', '--verbose', help="Verbose mode", action='store_true')
    parser.add_argument('-d', '--debug', help="Debug mode", action='store_true')
    parser.add_argument('-f', '--force', help="Force overwrite", action='store_true')
    parser.add_argument('-X', dest="force_cpp", help="Force C++", action='store_true')
    parser.add_argument('-H', dest="force_hpp", help="Force C++ with include", action='store_true')
    parser.add_argument('-C', dest="force_c", help="Force C", action='store_true')
    parser.add_argument('-l', dest="lang", metavar="LANG", help="Language selection", default="*")

    args = parser.parse_args()
    #print(args)

    if args.force_cpp or args.force_hpp: args.lang = "cpp14"
    if args.force_c: args.lang = "c"

    data = ""
    if args.url.startswith('http'):

        t = re.search(r"www\.hackerrank\.com/challenges/([^/]+)/", args.url)
        if t:
            contest = "master"
            challenge = t.group(1)
        else:
            t = re.search(r"www\.hackerrank\.com/contests/([^/]+)/challenges/([\w\d\-]+)", args.url)
            if t:
                contest = t.group(1)
                challenge = t.group(2)

        url = "https://www.hackerrank.com/rest/contests/{}/challenges/{}".format(contest, challenge)

        r = requests.get(url)
        if r.status_code == 200:
            data = r.text
    else:
        with open(args.url) as f:
            data = f.read()

    parser = HackerRankParser(args.debug)
    parser.feed(data)
    parser.info()
    parser.gen_stub(args.lang, args.force, args.force_hpp)
    parser.download(args.force)


if __name__ == '__main__':
    main()
