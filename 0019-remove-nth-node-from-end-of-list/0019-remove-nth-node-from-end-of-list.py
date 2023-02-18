# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        last = dummy.next
        left = dummy.next
        index = 1
        prev = dummy
        while last:
            if index > n:
                prev = prev.next
                left = left.next
            index += 1
            last = last.next
        
        prev.next = left.next
        return dummy.next
            
        