# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        duplicate = 101
        left = head
        if left:
            right = left.next
            while right:
                if left.val == right.val:
                    duplicate = left.val
                    prev.next = right
                else:
                    if duplicate == left.val:
                        prev.next = right
                    else:
                        prev = prev.next
                left = right
                right = right.next
            if duplicate == left.val:
                prev.next = right
        return dummy.next
        