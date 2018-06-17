# Mathematics > Number Theory > Manasa loves Maths
# Find out if any permutation of the given number is divisible by 8.
#
# https://www.hackerrank.com/challenges/manasa-loves-maths/problem
# https://www.hackerrank.com/contests/mar14/challenges/manasa-loves-maths
# challenge id: 1892
#

# here is my algorithm:
# if len(n) < 3: test directly with %
# if len(n) >= 3:
#   A number is divisble by 8 if its three last digits form a number that is
#   divisible by 8. In other words, a permutation of the input is divisible
#   by 8 if the input contains the digits of a 3-digit number divisible by 8.
#   Thus, no need to compute all the permutations.
#   Step 1:
#     precalculate all the 125 3-digit numbers divisible by 8 and compute
#     a kind of signature: each unique digit is a bit (30 bits in total)
#            0   1   2   3   4   5   6   7   8   9
#           ... ... ... ... ... ... ... ... ... ...
#           ^^^
#           001  if there is one 0
#           011  if there is two 0
#           111  if there is three 0
#   Step 2:
#     compute the same signature (limiting digit count to 3) for the tests
#     and test against the precomputed values


div8 = set()
for i in range(0, 1000, 8):
    count = [0] * 10
    count[i % 10] += 1
    count[(i // 10) % 10] += 1
    count[(i // 100) % 10] += 1
    b = 0
    for j in count:
        b = (b << 3) + ((1 << j) - 1)
    div8.add(b)


for _ in range(int(input())):
    n = input()

    ok = False

    if len(n) == 1:
        ok = int(n) % 8 == 0

    elif len(n) == 2:
        ok = (int(n) % 8 == 0) or (int(n[::-1]) % 8 == 0)

    else:
        count = [0] * 10

        for c in list(n):
            d = int(c)
            if count[d] < 3: count[d] += 1

        b = 0
        for j in count:
            b = (b << 3) + ((1 << j) - 1)

        for i in div8:
            if (b & i) == i:
                ok = "YES"
                break

    print("YES" if ok else "NO")
