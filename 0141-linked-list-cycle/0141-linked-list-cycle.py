# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        while node:
            if node.val == float("inf"):
                return True
            if node.next == None:
                return False
            node.val = float("inf")
            node = node.next
        