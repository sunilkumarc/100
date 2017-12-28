# https://www.interviewbit.com/problems/all-factors/

'''
Given a number N, find all factors of N.

Example:

N = 6 
factors = {1, 2, 3, 6}
Make sure the returned array is sorted.
'''

import math

def allFactors(A):
    N = int(math.sqrt(A))
    res = set()
    res.add(1)
    res.add(A)
    
    for i in range(2, N+1):
        if A % i == 0:
            res.add(i)
            res.add(int(A/i))
            
    res = list(res)
    res.sort()
    return res

if __name__ == '__main__':
    N = int(input().strip())
    res = allFactors(N)

    print(res)
