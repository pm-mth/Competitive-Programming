# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.dummy = ListNode(-inf)
        node = head
        while node:
            temp = node
            node = node.next
            temp.next = None
            self.sortList(temp)
        
        return self.dummy.next
        
    def sortList(self, newNode):
        node = self.dummy
        prev = None
        append = False
        while node:
            if node.val <= newNode.val:
                prev = node
                node = node.next 
            else:
                append = True
                prev.next = newNode
                newNode.next = node
                break
                
        if not append:
            prev.next = newNode
   
    
        