# ProjectEuler+ > Project Euler #17: Number to Words
# Read the numbers
#
# https://www.hackerrank.com/contests/projecteuler/challenges/euler017
# challenge id: 2643
#


units = ['zero', 'one', 'two', 'three', 'four',
         'five', 'six', 'seven', 'eight', 'nine',
         'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
         'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
teens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def int2words(n):
    """
    https://en.wikipedia.org/wiki/English_numerals
    http://www.lexisrex.com/English-Numbers/
    """
    assert n >= 0

    if n < 20:
        return units[n]

    if n < 100:
        w = teens[n // 10 - 2]
        if n % 10 != 0:
            w += "-" + units[n % 10]
        return w

    if n < 1000:
        w = units[n // 100] + " hundred"
        if n % 100 != 0:
            w += " and " + int2words(n % 100)
        return w

    if n < 1000000:
        w = int2words(n // 1000) + " thousand"
        if n % 1000 != 0:
            w2 = int2words(n % 1000)
            if w2.find(" and ") == -1:
                w += " and " + w2
            else:
                w += " " + w2
        return w

    if n < 1000000000:
        q, r = divmod(n, 1000000)
        w = int2words(q) + " million"
        if r != 0:
            w += " " + int2words(r)
        return w

    else:
        q, r = divmod(n, 1000000000)
        w = int2words(q) + " billion"
        if r != 0:
            w += " " + int2words(r)
        return w


def euler017(n):
    return int2words(n).title().replace('-', ' ').replace(' And ', ' ')


for _ in range(int(input())):
    print(euler017(int(input())))
