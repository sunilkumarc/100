def getPossibleMoves(piles):
    count = 0
    for pile in piles:
        while (pile % 2) == 0 and (pile != 0):
            count += 1
            pile = pile/2

    return count

if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        piles = list(map(int, input().strip().split()))
        res = getPossibleMoves(piles)
        
        if res % 2 == 0:
            print('Alan')
        else:
            print('Charlie')