# https://www.hackerrank.com/contests/hourrank-15/challenges/an-interesting-game-1/

import collections
Q = int(input().strip())

def findMax(arr, sortedMap):
    while True:
        key, value = sortedMap.popitem()
        if value < len(arr):
            break
    return value, sortedMap

for _ in range(Q):
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))

    myMap = {}
    for i in range(len(arr)):
        myMap[arr[i]] = i

    sortedMap = collections.OrderedDict(sorted(myMap.items()))
    bobsTurn = 1
    while len(arr) > 0:
        print(sortedMap)
        maxElemIndex, sortedMap = findMax(arr, sortedMap)
        arr = arr[:maxElemIndex]
        bobsTurn *= -1

    if bobsTurn == 1:
        print('ANDY')
    else:
        print('BOB')
