# https://leetcode.com/problems/odd-even-linked-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        oddDummy = ListNode(None)
        evenDummy = ListNode(None)
        
        oddDummy.next = head
        evenDummy.next = head
        
        oddTail = oddDummy
        evenTail = evenDummy
        
        i = 1
        while head:
            if i % 2 == 1:
                oddTail.next = head
                oddTail = oddTail.next
            else:
                evenTail.next = head
                evenTail = evenTail.next
            head = head.next
            i += 1
        
        evenTail.next = None
        oddTail.next = evenDummy.next
        return oddDummy.next