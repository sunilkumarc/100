# Write a program to find all the unique triplets which add up to 0 in the given array

# http://www.geeksforgeeks.org/find-triplets-array-whose-sum-equal-zero/

import itertools

def getNewList(nums):
    myDict = dict()
    for num in nums:
        if num in myDict:
            myDict[num] += 1
        else:
            myDict[num] = 1
            
    newList = []
    for key in myDict:
        newList.append(key)
        if myDict[key] > 1:
            newList.append(key)
    
    if 0 in myDict and myDict[0] > 2:
        newList.append(0)
    
    return newList

def findTriplets(nums, N):
    nums = getNewList(nums)
    print(nums)
    res = []
    nums.sort()
    N = len(nums)
    for i in range(0, len(nums)-2):
        left = i+1
        right = N-1
        while left < right:
            SUM = nums[i] + nums[left] + nums[right]
            if SUM == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1  
            elif SUM < 0:
                left += 1
            else:
                right -=1
    
    res.sort()
    return list(item for item, _ in itertools.groupby(res))

if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    res = findTriplets(arr, len(arr))
    print(res)