def maxProductSubArray(arr, N):
    globalMax = 1
    localMax = 1
    start = end = 0
    localStart = localEnd = 0

    for i in range(len(arr)):
        if arr[i] > 0:
            localMax *= arr[i]
            if localMax > globalMax:
                globalMax = localMax
                start = localStart
                end = i
        else:
            localMax = 1
            i += 1
            localStart = i
        
    return globalMax, start, end

if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    maxProduct, start, end = maxProductSubArray(arr, len(arr))

    print(arr)
    print('Max Product :', maxProduct)
    print('Start :', start)
    print('End :', end)