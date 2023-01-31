# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        if head.next == None:
            return head
      
        left = head
        mid = left.next
        right = mid.next
        left.next = None
        while right:
            mid.next = left
            left = mid
            mid = right
            right = right.next
        mid.next = left
        head = mid
        return head
        