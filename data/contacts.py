# Contacts
# Create a Contacts application with the two basic operations: add and find.
#
# https://www.hackerrank.com/challenges/contacts/problem
#

# Nota: il y a trop de noms pour se contenter d'un algo trivial de recherche dans contacts

import bisect

contacts = []

for _ in range(int(input())):
    op, contact = input().split()

    if op == "add":
        bisect.insort(contacts, contact)
    elif op == "find":
        position = bisect.bisect_left(contacts, contact)
        n = 0
        while position < len(contacts) and contacts[position].startswith(contact):
            position += 1
            n += 1
        print(n)
