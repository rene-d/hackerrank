# Circular Array Rotation
# Print the elements in an array after 'm' right circular rotation operations.
#
# https://www.hackerrank.com/challenges/circular-array-rotation/problem
#

if __name__ == "__main__":
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))

    # fait la rotation circulaire
    # en Python, c'est ultra-simple
    k = n - k % n
    a = a[k:] + a[:k]

    for _ in range(q):
        i = int(input())
        print(a[i])
