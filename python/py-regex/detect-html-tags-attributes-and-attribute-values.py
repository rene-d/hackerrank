# Python > Regex and Parsing > Detect HTML Tags, Attributes and Attribute Values
# Parse HTML tags, attributes and attribute values in this challenge.
# 
# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem
# 

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print('-> {} > {}'.format(*attr))
        
html = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()
