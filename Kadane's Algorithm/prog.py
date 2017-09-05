# Program to find maximum sum subarray using Kadane's Algorithm
# http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

def findMaxsumSubArray(arr):
    maxSoFar = arr[0]
    maxEndingHere = arr[0]
    startIndex = endIndex = 0

    for i in range(1, len(arr)):
        if arr[i] >= maxEndingHere + arr[i]:
            maxEndingHere = arr[i]
            startIndex = i
        else:
            maxEndingHere = maxEndingHere + arr[i]

        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere
            endIndex = i
    
    return maxSoFar, startIndex, endIndex

if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    print(arr)
    maxSum, startIndex, endIndex = findMaxsumSubArray(arr)
    print('Max Sum :', maxSum)
    print('Start Index :', startIndex)
    print('End Index :', endIndex)