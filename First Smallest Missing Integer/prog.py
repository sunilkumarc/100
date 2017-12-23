# https://leetcode.com/problems/first-missing-positive/description/#

class Solution(object):
    def arrange(self, nums):
        i = 0
        N = len(nums)
        while i < N and nums[i] > 0:
            i += 1
        
        j = i + 1
        while j < N:
            if nums[j] > 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
            j +=1
        
        return nums, i
        
    def firstMissingPositive(self, nums):
        nums, size = self.arrange(nums)
        nums.insert(0, 0)
        
        for i in range(1, size+1):
            if abs(nums[i]) <= size and nums[abs(nums[i])] > 0:
                nums[abs(nums[i])] = - nums[abs(nums[i])]
        
        print(nums)
        
        for i in range(1, size+1):
            if nums[i] > 0:
                return i
        
        return size+1