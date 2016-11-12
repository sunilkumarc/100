import math
import sys

def sieveOfEratosthenes(N):
    isPrime = [1 for _ in range(N)]
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

def segmentedSieve(N):
    limit = int(math.sqrt(N))
    result = []
    primes = sieveOfEratosthenes(limit)
    result.append(primes)
    # print('Finding primes till', limit, ':', primes)
    low = limit + 1
    high = limit * 2
    while low < N:
        localPrimes = []
        isPrime = [1 for _ in range(limit)]
        for prime in primes:
            j = int(math.floor(low/prime)) * prime
            if j < low:
                j += prime
            while j <= high:
                isPrime[j-low] = 0
                j += prime

        for i in range(low, high+1):
            if isPrime[i-low] == 1:
                localPrimes.append(i)

        result.append(localPrimes)
        low += limit
        high += limit
        if high > N:
            high = N

    for item in result:
        print(item)

if __name__=='__main__':
    N = int(input('Enter N : ').strip())
    segmentedSieve(N)
