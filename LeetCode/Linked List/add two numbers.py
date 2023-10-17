# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = l1
        num1 = ""
        while node:
            num1 += str(node.val)
            node = node.next
        node = l2
        num2 = ""
       
        while node:
            num2 += str(node.val)
            node = node.next
        
        ans = int(num1) + int(num2)
        ans = str(ans)
        dummy = ListNode()
        head = dummy
        for s in ans:
            node = ListNode(int(s))
            head.next = node
            head = head.next
        
        return dummy.next
            
