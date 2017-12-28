# https://www.interviewbit.com/problems/merge-overlapping-intervals/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        inter = []
        res = []
        
        for i in intervals:
            inter.append((i.start, i.end))
            
        inter.sort()
        start = inter[0][0]
        end = inter[0][1]
        
        for i in xrange(1, len(inter)):
            a = inter[i][0]
            b = inter[i][1]
            if end >= a:
                if b > end:
                    end = b
            else:
                res.append(Interval(start, end))
                start = a
                end = b
                
        res.append(Interval(start, end))
        return res
    
