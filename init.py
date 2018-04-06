#! /usr/bin/env python3

import sys
from html.parser import HTMLParser
import requests
import os
import subprocess
import json
import urllib.parse
import pprint
import argparse
import platform


BASEURL = 'https://www.hackerrank.com'
DOMAINS = {'algorithms': 'algo',
           'cpp': 'cpp',
           'mathematics': 'math',
           'python': 'python',
           'data-structures': 'data',
           'fp': 'fp'}


class HackerRankParser(HTMLParser):

    def __init__(self, debug=False):
        super().__init__()
        self.testcases = ''
        self.pdf = ''
        self.link = ''
        self.name = ''
        self.fullname = []
        self.domain = ''
        self.key = ''
        self.initialData = None
        self.debug = debug
        self.details = {}

    def __repr__(self):
        return "\n".join([self.name, self.pdf, self.testcases, self.link, self.domain, self.key])

    def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)
        if tag == "a" :
            m = dict()
            for a, b in attrs:
                m[a] = b
            if 'data-analytics' in m:
                if m['data-analytics'] == 'ChallengeViewSidebarTestCases' and m['id'] == 'test-cases-link':
                    self.testcases = m['href']

                if m['data-analytics'] == 'ChallengeViewSidebarPDF' and m['id'] == 'pdf-link':
                    self.pdf = m['href']

                if m['data-analytics'] == 'ChallengeViewTab' and m['class'] == "hr-problem-link":
                    self.link = m['href']

                if m['data-analytics'] == 'Breadcrumb' and m['data-attr2'] == 'global':
                    self.name = name = m['data-attr1']
                    if name != 'Dashboard':
                        self.fullname.append(name)
                    u = m['href']
                    if u.startswith('/domains/') and u[9:].find('/') == -1:
                        self.domain = u[9:]
                    if u.startswith('/challenges/') and u[12:].find('/') == -1:
                        self.key = u[12:]

        elif tag == "script":
            m = dict()
            for a, b in attrs:
                m[a] = b
            if 'type' in m and 'id' in m:
                if m['type'] == "application/json" and m['id'] == "initialData":
                    self.initialData = []

    def handle_endtag(self, tag):
        if self.initialData is not None and tag == "script":
            data = urllib.parse.unquote(''.join(self.initialData))
            if self.debug:
                with open("initialData.json", "w") as f:
                    f.write(data)
                print("DEBUG: write initialData.json")
            data = json.loads(data)

            self.details = {}
            for k, v in  data["community"]["challenges"]["challenge"].items():
                self.details = v['detail']
                break

            self.initialData = None

    def handle_data(self, data):
        if self.initialData is not None:
            self.initialData.append(data)

    def info(self):
        print("Name   :", self.name)
        print("Link   :", self.link)
        print("Path   :", ' > '.join(self.fullname))
        print("Domain :", self.domain)
        print("Key    :", self.key)

    def info2(self):
        """ affiche des infos détaillées de initialData """
        v = self.details

        remove_keys = ['body_html', 'primary_contest', 'custom_tabs']
        show_keys = ['contest_slug', 'slug', 'difficulty_name', 'languages', 'name', 'preview',
                        'python3_template', 'python3_template_head', 'python3_template_tail',
                        'cpp14_template',
                        'cpp14_template_head', 'cpp14_template_tail',
                        'cpp14_skeliton_head', 'cpp14_skeliton_tail']

        for i in remove_keys:
            if i in v:
                del v[i]

        for i in show_keys:
            if i in v:
                print("{:<20} = {}".format(i, v[i]))

        #pprint.pprint(v)


    def gen_stub(self, lang, overwrite=False, hpp=False):

        EXTENSIONS = {"cpp": "cpp",
                      "cpp14": "cpp",
                      "c": "c",
                      "python3": "py",
                      "haskell": "hs"}

        if lang == "*":
            if 'languages' in self.details:
                languages = self.details['languages']
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

        os.makedirs(os.path.join(os.path.dirname(__file__), domain), exist_ok=True)

        filename = os.path.join(os.path.dirname(__file__), domain, self.key + "." + extension)
        if not overwrite and os.path.exists(filename):
            print("File exists:", filename)
            return
        cmake = os.path.join(os.path.dirname(__file__), domain, "CMakeLists.txt")


        def write_header(f, comment, add_skeliton=True):

            def line(text=None):
                if text is None:
                    f.write('\n')
                else:
                    f.write(comment + text + '\n')

            def skeliton(what):
                text = self.details.get(lang + "_" + what, "").strip()
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


            line(self.name)
            if 'preview' in self.details:
                line(self.details['preview'])
            line('')
            line('{}{}'.format(BASEURL, self.link))
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
        r = requests.get(args.url)
        #print("ok", r.headers['content-type'])
        if r.status_code == 200:
            data = r.text
    else:
        with open(args.url) as f:
            data = f.read()

    parser = HackerRankParser(args.debug)
    parser.feed(data)
    parser.info()
    if args.verbose:
        parser.info2()
    parser.gen_stub(args.lang, args.force, args.force_hpp)


if __name__ == '__main__':
    main()


""" Données exploitables
{
    "community": {
        "challenges": {
            "challenge": {
                "master/time-conversion": {
                    "detail": {
                        "contest_slug": "master",
                        "slug": "time-conversion",
                        "name": "Time Conversion",
                        "preview": "Convert time from an AM/PM format to a 24 hour format.",
                        "level": 8,
                        "languages": [
                            "c",
                            "cpp",
                            "python3",
                            "cpp14",
                        ],
                        "difficulty_name": "Easy",
                        "default_language": null,
                        "python3_template": "#!/bin/python3\n\nimport sys\n\ndef timeConversion(s):\n    # Complete this function\n\ns = input().strip()\nresult = timeConversion(s)\nprint(result)\n",
                        "python3_template_head": "",
                        "python3_template_tail": "",
                        "cpp14_template": "#include <bits/stdc++.h>\n\nusing namespace std;\n\nstring timeConversion(string s) {\n    // Complete this function\n}\n\nint main() {\n    string s;\n    cin >> s;\n    string result = timeConversion(s);\n    cout << result << endl;\n    return 0;\n}",
                        "body_html": ....,
                        "description": ....,
                    },
                }
            }
        },
"""

"""

https://www.hackerrank.com/rest/contests/projecteuler/challenges/euler016
https://www.hackerrank.com/rest/contests/master/challenges/the-birthday-bar


https://www.hackerrank.com/rest/contests/master/
"""