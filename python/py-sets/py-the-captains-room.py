# Python > Sets > The Captain's Room
# Out of a list of room numbers, determine the number of the captain's room.
#
# https://www.hackerrank.com/challenges/py-the-captains-room/problem
#

k = int(input())
rooms = list(map(int, input().split()))

a = set()
room_group = set()

for room in rooms:
    if room in a:
        room_group.add(room)
    else:
        a.add(room)

a = a - room_group
print(a.pop())
