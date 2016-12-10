Q = int(input().strip())

maxArray = []
maxIndex = 0

def initMaxArrayAndIndex(arr):
    global maxArray

    for i in range(len(arr)):
        print(arr[i])
        maxArray[arr[i]] = i

def findMax(arr):
    global maxArray
    global maxIndex

    while maxIndex >= 0:
        if maxArray[maxIndex] != -1 and len(arr) > maxArray[maxIndex]:
            break
        maxIndex -= 1

    res = maxArray[maxIndex]
    maxIndex -= 1
    return res

for _ in range(Q):
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))

    # global maxArray
    # global maxIndex

    maxArray = [-1 for _ in range(1000000001)]
    maxIndex = 1000000000

    initMaxArrayAndIndex(arr)
    bobsTurn = 1
    while len(arr) > 0:
        maxElem = findMax(arr)
        arr = arr[:maxElem]
        bobsTurn *= -1

    if bobsTurn == 1:
        print('ANDY')
    else:
        print('BOB')
