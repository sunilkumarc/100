# https://www.hackerearth.com/challenge/competitive/june-circuits-17/algorithm/jump-out-34/
N = int(input().strip())
boosters = list(map(int, input().strip().split()))

def getSteps(N, boosters):
    for i in range(N):
        if boosters[i] >= N-i:
            return i+1

    return N

print(getSteps(N, boosters))
