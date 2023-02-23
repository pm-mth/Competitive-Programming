# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        if head == None:
            return head
        dummy = ListNode(0, head)
        end = head
        first = head
        prev = head
        count = 1
        while end.next:
            if count >= k:
                first = first.next
            if count > k:
                prev = prev.next
                
            count += 1
            end = end.next
            
        if k > count:
            end = head
            first = head
            prev = head
            while k > count:
                k = k % count
            if k == 0:
                return head
            count = 1
            while end.next:
                if count >= k:
                    first = first.next
                if count > k:
                    prev = prev.next
                count += 1
                end = end.next
        
        if end.next == None and first == head:
            return head
        dummy.next = first
        prev.next = None
        end.next = head
        return dummy.next
                
            
        