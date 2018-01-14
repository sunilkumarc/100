# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(None)
        dummy.next = head
        one = two = dummy
        
        while n > 0:
            one = one.next
            n -= 1
        
        while one.next:
            one = one.next
            two = two.next
        
        if two.val == None:
            return head.next
        
        two.next = two.next.next
        return dummy.next