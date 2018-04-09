# XML 1 - Find the Score
# Learn about XML parsing in Python.
#
# https://www.hackerrank.com/challenges/xml-1-find-the-score/problem
#

import sys
import xml.etree.ElementTree as etree
# (skeliton_head) ----------------------------------------------------------------------


# version récursive
def get_attr_number(node):
    nb = len(node.attrib)
    for i in node:
        nb += get_attr_number(i)
    return nb


# version non récursive: traverse tout l'arbre XML séquentiellement
def get_attr_number(node):
    return sum(len(i.attrib) for i in node.iter())


# (skeliton_tail) ----------------------------------------------------------------------
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
