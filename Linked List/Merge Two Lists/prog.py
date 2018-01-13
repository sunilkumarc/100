# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def recursive(self, l1, l2, tail):
        if not l2:
            tail.next = l1
            return
        
        elif not l1:
            tail.next = l2
            return
        
        if l1.val <= l2.val:
            temp = l1.next
            tail.next = l1
            tail = tail.next
            l1.next = None
            l1 = temp
        else:
            temp = l2.next
            tail.next = l2
            tail = tail.next
            l2.next = None
            l2 = temp
        
        self.recursive(l1, l2, tail)
    
    def iterative(self, l1, l2):
        dummy = ListNode(None) 
        tail = dummy
        
        while True:
            if not l2:
                tail.next = l1
                break
            elif not l1:
                tail.next = l2
                break
            
            if l1.val <= l2.val:
                temp = l1.next
                tail.next = l1
                tail = tail.next
                l1.next = None
                l1 = temp
            else:
                temp = l2.next
                tail.next = l2
                tail = tail.next
                l2.next = None
                l2 = temp
        
        return dummy.next
        
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(None)
        tail = dummy
        self.recursive(l1, l2, tail)
        return dummy.next