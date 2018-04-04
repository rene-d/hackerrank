# Beautiful Binary String
#  How many binary characters must you change to remove every occurrence of "010" from a binary string?
#
# https://www.hackerrank.com/challenges/beautiful-binary-string/problem
#

# deux opérations suffisent à enlever le motif 010
#   01010 -> 01110
#   010 -> 000

# pour dénombrer, il suffit donc de compter le nombre d'occurences de 010 qui ne se recouvrent pas

def beautifulBinaryString(b):
    n = 0

    while True:
        p = b.find('01010')
        if p == -1: break
        b = b[:p + 2] + '1' + b[p + 3:]
        n += 1

    while True:
        p = b.find('010')
        if p == -1: break
        b = b[:p + 1] + '0' + b[p + 2:]
        n += 1

    return n

if __name__ == "__main__":
    n = int(input().strip())
    b = input().strip()
    result = beautifulBinaryString(b)
    print(result)
