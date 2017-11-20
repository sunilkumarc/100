# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/

################################################################
#                   NORMAL WAY (Some test fail)
################################################################
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

################################################################
#                   DYNAMIC PROGRAMMING
################################################################
def findLength(A, B):
        A.insert(0, 0)
        B.insert(0, 0)
        m = len(A)
        n = len(B)
        maxLen = 0
        
        dp = [[0 for x in range(m)] for y in range(n)]
        
        for row in range(1, n):
            for col in range(1, m):
                if A[col] == B[row]:
                    dp[row][col] = dp[row-1][col-1] + 1
                    maxLen = max(maxLen, dp[row][col])
        
        return maxLen

################################################################

if __name__ == '__main__':
    arr1 = list(map(int, input().strip().split()))
    arr2 = list(map(int, input().strip().split()))

    # arr, len = findMaxRepeatingSubarray(arr1, arr2)
    maxLen = findLength(arr1, arr2)
    print(maxLen)