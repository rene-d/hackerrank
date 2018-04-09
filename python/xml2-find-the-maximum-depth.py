# XML2 - Find the Maximum Depth
# Find the maximum depth in an XML document.
#
# https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem
#

import xml.etree.ElementTree as etree
# (skeliton_head) ----------------------------------------------------------------------

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    maxdepth = max(maxdepth, level + 1)
    for node in elem:
        depth(node, level + 1)



# (skeliton_tail) ----------------------------------------------------------------------
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
