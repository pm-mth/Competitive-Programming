# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: 
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        odd = head
        if odd:
            firstEven = odd.next
            even = firstEven
            
        while even:
            oddOne = even.next
            if oddOne:
                evenOne = oddOne.next
                even.next = evenOne
                odd.next = oddOne
                oddOne.next = firstEven
                odd = oddOne
                even = evenOne
                
            if even and even.next == None:
                even = even.next
        return head
        