# https://www.interviewbit.com/problems/largest-number/

'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example:
Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
'''

class Solution:
    def compare(self, x, y):
        one = int(str(x) + str(y))
        two = int(str(y) + str(x))
        if one > two:
            return 1
        return -1
        
    def largestNumber(self, A):
        r = sorted(A, cmp=self.compare)
        r.reverse()
        res = ''
        for num in r:
            res += str(num)
        
        res = res.lstrip('0')
        
        if res == '':
            return '0'
            
        return res
