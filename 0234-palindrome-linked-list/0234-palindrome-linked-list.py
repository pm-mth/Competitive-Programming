# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        count = 0
        while node:
            node= node.next
            count += 1
        
        mid = count//2
        right = head
        l = 0
        left = []
        while l < mid and right:
            left.append(right.val)
            right = right.next
            l += 1
        if count%2 == 1:
            right = right.next
        
        start = 0
        while right and start < mid:
            if right.val != left[-1-start]:
                return False
            right = right.next
            start += 1
        return True
            
        
            
        
      
            
            
            
            
            
        
        
        