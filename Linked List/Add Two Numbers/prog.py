# https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        prevNode = nextNode = None
        currNode = head
        
        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        
        return prevNode
        
    def addTwoNumbers(self, l1, l2):
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        dummy = ListNode(None)
        tail = dummy
        
        carry = 0
        while l1 and l2:
            s = l1.val + l2.val + carry
            node = ListNode(s%10)
            tail.next = node
            tail = tail.next
            carry = int(s/10)
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            s = l1.val + carry
            node = ListNode(s%10)
            tail.next = node
            tail = tail.next
            carry = int(s/10)
            l1 = l1.next
        
        while l2:
            s = l2.val + carry
            node = ListNode(s%10)
            tail.next = node
            tail = tail.next
            carry = int(s/10)
            l2 = l2.next
        
        if carry > 0:
            node = ListNode(carry)
            tail.next = node
        
        return self.reverseList(dummy.next)