#! /usr/bin/env python3

"""
HackerRank testcases downloader
"""

import argparse
import zipfile
import os
import requests
import re


parser = argparse.ArgumentParser(description='Download testcases (practice challenges only).')
parser.add_argument('name', help="Challenge name")
parser.add_argument('url', nargs='*', help="test case url")

args = parser.parse_args()

name = re.sub(r'^.*\.hackerrank\.com/challenges/([\w\d\-].*)/.*$', r'\1', args.name)

zip = os.path.join(os.path.dirname(__file__), "testcases2", "master", name + "-testcases.zip")

if not os.path.exists(zip):
    print("create", zip)
    z = zipfile.ZipFile(zip, mode="w", compression=zipfile.ZIP_DEFLATED)
else:
    print("open", zip)
    z = zipfile.ZipFile(zip, mode="a", compression=zipfile.ZIP_DEFLATED)


def add_testcase(url):
    m = re.search(r'(in|out)put\d\d\.txt', url)
    if m:
        arcname = m.group(0)
        if arcname.startswith("input"):
            arcname = "input/" + arcname
        elif arcname.startswith("output"):
            arcname = "output/" + arcname

        data = requests.get(url)

        print("Add {} size {} into archive".format(arcname, len(data.content)))
        z.writestr(arcname, data.content)

    else:
        m = re.search(r'([io])(\d+)', url)
        if m:
            if m.group(1) == 'i':
                arcname = "input/input"
            else:
                arcname = "output/output"
            arcname += "{:02d}.txt".format(int(m.group(2)))

            print("Enter data for {}, terminate with a empty line".format(arcname))
            data = ""
            while True:
                s = input().strip()
                if s == "":
                    break
                data += s + "\n"

            print("Add {} size {} into archive".format(arcname, len(data)))
            z.writestr(arcname, data)


if len(args.url) == 0:
    while True:
        url = input("url> ").strip()
        if url == "":
            break
        add_testcase(url)
else:
    for url in args.url:
        add_testcase(url)

print()
z.printdir()
# for e in z.infolist():
#     print("{} {:10} {:10} {}".format(e.date_time, e.compress_size, e.file_size, e.filename))

z.close()
