# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        node = head
        while node:
            newNode = ListNode(node.val)
            newNode.next = newHead
            newHead = newNode
            node = node.next
        
        return newHead
#         if not head:
#             return head
#         self.newHead = None
#         def solve(node):
#             if not node:
#                  return node
#             if not node.next:
#                 self.newHead = node
#                 return node
            
#             last = solve(node.next)
#             last.next = node
#             node.next = None
#             return node
#         solve(head)
#         return self.newHead
            
    
        
