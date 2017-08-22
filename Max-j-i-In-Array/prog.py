# http://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/

def findMaxji(arr, N):
    LMin = []
    LMax = []
    minimum = arr[0]
    LMin.append(minimum)
    for i in range(1, N):
        minimum = min(minimum, arr[i])
        LMin.append(minimum)

    maximum = arr[N-1]
    LMax.append(maximum)
    for j in range(N-2, -1, -1):
        maximum = max(maximum, arr[j])
        LMax.append(maximum)
    LMax.reverse()

    i = j = 0
    maxji = -1
    while i < N and j < N:
        if LMin[i] < LMax[j]:
            maxji = max(maxji, j-i)
            j += 1
        else:
            i += 1

    return maxji

if __name__ == '__main__':
    T = int(input().strip())
    print('\nProgram to print maximum j-i in an array such that arr[j] > arr[i]\n')
    for _ in range(T):
        arr = input().strip().split()
        res = findMaxji(arr, len(arr))
        print(arr, ' -> ', res)
