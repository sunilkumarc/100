# Go thill the square root of the number
# If i divides N, then N/i also divides N

def factors(N):
    i = 1
    factors = []
    while i*i <= N:
        if N % i == 0:
            factors.append(i)
            factors.append(int(N/i))
        i += 1

    factors.sort()
    return factors

if __name__ == '__main__':
    N = int(input('Enter N : '))
    print(factors(N))
