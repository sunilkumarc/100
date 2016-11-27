# https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/little-ashish-and-his-wife/

if __name__=='__main__':
    T = int(input().strip())
    for _ in range(T):
        N, X = map(int, input().strip().split())
        prices = input().strip().split()
        N = len(list(set(prices)))
        if N == X:
            print('Perfect husband')
        elif N > X:
            print('Lame husband')
        elif N < X:
            print('Bad husband')
