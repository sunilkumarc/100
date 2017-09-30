def getBuildings(buildings, K):
    count = 0
    i = 0
    size = len(buildings)
    while i < N and buildings[i] >= K:
        if buildings[i] % K == 0:
            count += 1
        i += 1

    return count

if __name__ == '__main__':
    N = int(input().strip())
    buildings = []
    for _ in range(N):
        buildings.append(int(input().strip()))
    
    buildings.sort(reverse=True)
    preComputed = dict()

    Q = int(input().strip())
    for _ in range(Q):
        K = int(input().strip())
        if K in preComputed:
            print(preComputed[K])
        else:
            res = getBuildings(buildings, K)
            preComputed[K] = res
            print(res)