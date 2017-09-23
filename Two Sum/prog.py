# Program to find indices of two integers adding up to a target sum in the given array
# https://leetcode.com/problems/two-sum/description/

def twoSum(nums, target):
    diffs = dict()
    res = []
    for i in range(len(nums)):
        diffs[target-nums[i]] = i
    
    for i in range(len(nums)):
        if nums[i] in diffs and i != diffs[nums[i]]:
            res.append(i)
            res.append(diffs[nums[i]])
            return res
    
    return res

if __name__ == '__main__':
    nums = list(map(int, input().strip().split()))
    target = int(input().strip())
    res = twoSum(nums, target)
    print(res)