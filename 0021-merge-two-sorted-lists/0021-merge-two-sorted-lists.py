# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        newNode = dummy
        node1 = list1
        node2 = list2
        while node1 and node2:
            if node1.val <= node2.val:
                newNode.next = node1
                node1 = node1.next
                newNode = newNode.next
            else:
                newNode.next = node2
                node2 = node2.next
                newNode = newNode.next
        if node1:
            newNode.next = node1
        elif node2:
            newNode.next = node2
        return dummy.next
                
                
                
                
        