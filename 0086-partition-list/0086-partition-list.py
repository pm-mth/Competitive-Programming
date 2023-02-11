# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        
        
        dummygreat = ListNode()
        dummyless = ListNode()
        
        node = head
        less = dummyless
        great = dummygreat
        while node:
            newNode = ListNode(node.val)
            if node.val < x:
                less.next = newNode
                less = newNode
            else:
                great.next = newNode
                great = newNode
            node = node.next
        less.next = dummygreat.next
        return dummyless.next
        
            
        
       