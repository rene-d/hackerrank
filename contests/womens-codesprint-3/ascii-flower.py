# Women's CodeSprint 3 > ASCII Flower
# Help Julie design draw an ASCII flower pattern spanning a given number of rows and columns.
#
# https://www.hackerrank.com/contests/womens-codesprint-3/challenges/ascii-flower
#

flower = ['..O..',
          'O.o.O',
          '..O..']
r, c = map(int, input().split())
for _ in range(r):
    for i in range(3):
        print(flower[i] * c)
