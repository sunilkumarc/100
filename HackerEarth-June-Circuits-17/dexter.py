# https://www.hackerearth.com/challenge/competitive/june-circuits-17/algorithm/dexter-plays-with-gp-1/
import math
store = dict()

def getN(r, S, p):
    global store
    a = [0, 1]
    if r in store:
        a = store[r]
        
    if sum(a)%p == S:
        return len(a) - 1
    
    end = p
    if len(a)-1 < p:
        end = len(a) 

    for N in range(1, end):
        if sum(a[:(N+1)]) % p == S:
            return N-1

    for N in range(end, p):
        a.append((a[N-1] * r) % p)  
        if sum(a)%p == S:
            return len(a) - 1
    
    return -1

T = int(input().strip())

for i in range(T):
    r, S, p = map(int, input().strip().split())
    
    print(getN(r, S, p))