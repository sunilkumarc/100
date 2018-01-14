# https://leetcode.com/problems/reverse-linked-list-ii/description/

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
        
    def reverseBetween(self, head, m, n):
        dummy = ListNode(None)
        dummy.next = head
        prevNode = nextNode = None
        one = two = dummy
        if m == n:
            return head
        
        while two and n > 0:
            if m > 0:
                prevNode = one
                one = one.next
                m -= 1  
            if n > 0:
                two = two.next
                n -= 1
        
        nextNode = two.next
        two.next = None
        start = self.reverseList(one)
        
        one.next = nextNode
        prevNode.next = start
        
        if prevNode.val != None:
            return head
        
        return prevNode.next