# Python > Regex and Parsing > HTML Parser - Part 2
# Parse HTML comments and data using HTML Parser.
# 
# https://www.hackerrank.com/challenges/html-parser-part-2/problem
# 

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  
    def handle_comment(self, data):
        if data.find('\n') >= 0:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        print(data)

    def handle_data(self, data):
        if data.strip() != "":
            print(">>> Data")
            print(data)
  
  
html = ""       
for i in range(int(input())):
    html += input()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

