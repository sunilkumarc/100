Q = int(input().strip())

for _ in range(Q):
    A, B, C = map(int, input().strip().split())

    aDist = abs(A-C)
    bDist = abs(B-C)
    if aDist == bDist:
        print('Mouse C')
    elif aDist < bDist:
        print('Cat A')
    else:
        print('Cat B')
