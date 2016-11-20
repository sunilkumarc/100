# https://www.hackerearth.com/november-circuits/algorithm/fredo-is-in-a-hurry/
import math

def stairCaseTime(floor): return floor * (floor + 1) / 2

def getTime(N):
    result = 0
    X = 0
    if N == 1:
        return 1
    startFrom = int(math.sqrt(N))
    liftTime = N - startFrom
    while stairCaseTime(startFrom) <= liftTime:
        startFrom += 1
        liftTime -= 1

    startFrom -= 1
    return (N-startFrom)*2

if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        print(getTime(N))
