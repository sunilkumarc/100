def repeatedNumber(A):
    xor = A[0]
    N = len(A)
    
    for i in range(1, N):
        xor ^= A[i]
    
    for i in range(1, N+1):
        xor ^= i
    
    set_bit = xor & ~(xor-1)
    
    y = 0
    for num in A:
        if not num & set_bit:
            y ^= num
            
    for i in range(1, N+1):
        if not i & set_bit:
            y ^= i
    
    x = xor ^ y
    for num in A:
        if num == y:
            x, y = y,x
            
    res = [x, y]
    
    return res

if __name__ == '__main__':
    A = list(map(int, input().strip().split()))
    print(A)
    res = repeatedNumber(A)

    print('Repeated :', res[0])
    print('Missing :', res[1])
