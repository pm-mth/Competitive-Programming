# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node = head
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        maxTwin = 0
        n = len(arr)
        for i in range(n//2):
            curSum = arr[i] + arr[n-1-i]
            maxTwin = max(maxTwin, curSum)
        return maxTwin
            
        