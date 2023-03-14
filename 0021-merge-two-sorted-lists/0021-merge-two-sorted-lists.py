# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head =  ListNode()
        node = head
        self.merge(node, list1, list2)
        return head.next
        
    def merge(self, node, node1, node2):
        if node1 and not node2:
            node.next = node1
        if node2 and not node1:
            node.next = node2
        
        if node1 and node2:
            if node1.val < node2.val:
                node.next = node1
                self.merge(node.next, node1.next, node2)
            else:
                node.next = node2
                self.merge(node.next, node1, node2.next)
                
    

        
        
        
   
            
            
            
       
                
                
                
        