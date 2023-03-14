# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        return self.divideAndConquer(head)
        
        
    def divideAndConquer(self, node):
        if not node or not node.next:
            return node
        
       
        #divide the nodes into half in each recursion
        prev = None
        slow = node
        fast = node
        
        while fast and fast.next:
            prev = slow
            slow = slow.next 
            fast = fast.next.next
        if prev:
            prev.next = None

        left = self.divideAndConquer(node)
        right = self.divideAndConquer(slow)
        
        
        #merge the list nodes
        dummy = ListNode()
        newNode = dummy
        while left and right:
            if left.val < right.val:
                newNode.next = left
                left = left.next
            else:
                newNode.next = right
                right = right.next
            newNode = newNode.next
       
        newNode.next = left or right
        
        return dummy.next
                
                
        
        