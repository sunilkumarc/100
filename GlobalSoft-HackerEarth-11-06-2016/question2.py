import math
import sys

def sieveOfEratosthenes(N):
    isPrime = [1 for _ in range(N+1)]
    i = 2
    while i <= math.sqrt(N):
        if isPrime[i] == 1:
            j = i * 2
            while j < N:
                isPrime[j] = 0
                j += i
        i += 1

    primes = []
    for i in range(2, N):
        if isPrime[i] == 1:
            primes.append(i)

    return primes

if __name__=='__main__':
    T = int(input().strip())

    for _ in range(T):
        N, L, R = map(int, input().strip().split())
        primes = sieveOfEratosthenes(N)
        print(primes)
        # segmentedSieve(N, L, R)
