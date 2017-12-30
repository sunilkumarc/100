# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        if head == None:
            return
        
        pre = None
        cur = head

        while cur != None:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        
        return pre