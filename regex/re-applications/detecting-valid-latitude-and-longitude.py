# Regex > Applications > Detecting Valid Latitude and Longitude Pairs
# Can you detect the Latitude and Longitude embedded in text snippets, using regular expressions?
#
# https://www.hackerrank.com/challenges/detecting-valid-latitude-and-longitude/problem
# https://www.hackerrank.com/contests/regex-practice-1/challenges/detecting-valid-latitude-and-longitude
# challenge id: 1086
#

import re

for _ in range(int(input())):
    s = input()

    ok = re.match(r'''
^\(                                     # ( au début
   [+-]?                                # signe optionnel
   (90(\.0+)?                           # 90 ou 90.0000...
    | ( ([0-9]|[0-8][0-9])              # 0 à 89
        (\.\d+)?                        # .1234567890
      )
   )
   ,\s?                                 # ", " ou ","
   [+-]?                                # signe optionnel
   (180(\.0+)?                          # 180 ou 180.000...
    | ( ([0-9]|[1-9][0-9]|1[0-7][0-9])  # 0 à 179
        (\.\d+)?                        # décimales
      )
   )
\)$                                     # ) finale
''', s, re.VERBOSE)

    print('Valid' if ok else 'Invalid')
