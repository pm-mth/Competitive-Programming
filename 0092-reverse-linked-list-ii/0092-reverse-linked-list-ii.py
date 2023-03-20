# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        count = 1
        prev = dummy
        cur = dummy.next
        while count <= right :
            if count == left :
                leftNode = cur
                
            if count < left:
                prev = prev.next
            if count == right:
                rightNode = cur.next
                cur.next = None
            
            cur = cur.next
            count += 1
        
    
        
        newHead, newTail = self.reverse(leftNode)
        prev.next = newHead
        newTail.next = rightNode
        return dummy.next
        
        
       
    def reverse(self, head):
        if not head or not head.next:
            return head, head
        prev = None
        cur = head
        nextNode = cur.next
        while cur:
            cur.next = prev
            prev = cur
            cur = nextNode
            if cur:
                nextNode = nextNode.next
        
      
        return prev, head
        
        
                
        