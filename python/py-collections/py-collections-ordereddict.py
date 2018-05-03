# Python > Collections > Collections.OrderedDict()
# Print a dictionary of items that retains its order.
#
# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
#

from collections import OrderedDict

prices = OrderedDict()

for _ in range(int(input())):
    item, price = input().rsplit(maxsplit=1)
    prices[item] = prices.get(item, 0) + int(price)

for item, price in prices.items():
    print(item, price)
