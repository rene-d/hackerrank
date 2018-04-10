# Viral Advertising
#  How many people will know about the new product after n days?
#
# https://www.hackerrank.com/challenges/strange-advertising/problem
#

def viralAdvertising(n):
    people = 5                  # jour 1: 5 personnes reçoivent la pub
    like = 0
    for _ in range(n):
        people = people // 2    # la moitié like et retransmettent ...
        like += people          # on compte les personnes qui like
        people = people * 3     # ... à 3 autres personnes
    return like


if __name__ == "__main__":
    n = int(input())
    result = viralAdvertising(n)
    print(result)
