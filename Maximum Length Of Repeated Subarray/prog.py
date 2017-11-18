# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
# INCOMPLETE - 37/54 passing

def findSubarrays(arr):
    N = len(arr)
    res = []
    for i in range(N):
        for j in range(i+1, N+1):
            res.append(arr[i:j])
    
    return res


def findMaxRepeatingSubarray(arr1, arr2):
    subarr1 = findSubarrays(arr1)
    subarr2 = findSubarrays(arr2)

    subarr1.sort(key = len, reverse=True)
    for arr in subarr1:
        if arr in subarr2:
            return arr, len(arr)

    return None, -1


if __name__ == '__main__':
    arr1 = list(map(int, input().strip().split()))
    arr2 = list(map(int, input().strip().split()))

    arr, len = findMaxRepeatingSubarray(arr1, arr2)
    print(arr, len)