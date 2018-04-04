# Sorting: Bubble Sort
# Find the minimum number of conditional checks taking place in Bubble Sort
# 
# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
#

n = int(input())
a = list(map(int, input().split()))

swaps = 0
while True:
    swapped = False
    i = 0
    while i < n - 1:
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            swaps += 1
            swapped = True            
        i += 1
    if not swapped:
        break
        
print("Array is sorted in {} swaps.".format(swaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))

