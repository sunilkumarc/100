# https://www.hackerrank.com/contests/hourrank-15/challenges/an-interesting-game-1/

Q = int(input().strip())

for _ in range(Q):
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))

    count = 1
    currMax = arr[0]
    for i in range(1, N):
        if arr[i] > currMax:
            count += 1
            currMax = arr[i]

    if count % 2 == 0:
        print('ANDY')
    else:
        print('BOB')
