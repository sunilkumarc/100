'''
Problem : https://www.hackerearth.com/euromonitor-international-hiring-challenge/problems/5eba5740e33542dda3ed17422080d3c8/
'''

def getXOR(arr):
    result = 0
    for elem in arr:
        result ^= elem
    return result

def findSubArray(N, Z, arr):
    N = int(N)
    Z = int(Z)
    subArr = arr[0:Z]
    minXOR = getXOR(subArr)
    leastXORIndex = 0
    i = 1
    localMinXOR = minXOR
    while i <= N-Z:
        localMinXOR = localMinXOR ^ subArr[0] ^ arr[i+Z-1]
        subArr.pop(0)
        subArr.append(arr[i+Z-1])
        if localMinXOR <= minXOR:
            minXOR = localMinXOR
            leastXORIndex = i
        i += 1

    return leastXORIndex

if __name__ == '__main__':
    T = int(input().strip())
    for i in range(T):
        N, Z = input().strip().split(' ')
        arr = [int(elem) for elem in input().strip().split(' ')]

        print(findSubArray(N, Z, arr)+1)
        # print(findSubArray(N, Z, arr)+1)
    # K = int(input('Enter K : '))
    # printSubArrays(K)
