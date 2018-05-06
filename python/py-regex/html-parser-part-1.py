# Python > Regex and Parsing > HTML Parser - Part 1
# Parse HTML tags, attributes and attribute values using HTML Parser.
# 
# https://www.hackerrank.com/challenges/html-parser-part-1/problem
# 


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):        
        print('Start :',tag)
        for e in attrs:
            print('->', e[0],'>', e[1])
            
    def handle_endtag(self, tag):
        print('End   :', tag)
        
    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        for e in attrs:
            print ('->', e[0], '>', e[1])
            
parser = MyHTMLParser()
parser.feed(''.join([input() for _ in range(int(input()))]))
parser.close()
