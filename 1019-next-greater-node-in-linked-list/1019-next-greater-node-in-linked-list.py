# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        node = head
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        
        stack = []
        for i in range(len(arr)):
            while stack and arr[i] > arr[stack[-1]]:
                arr[stack.pop()] = arr[i]
            
            stack.append(i)
        while stack:
            arr[stack.pop()] = 0
            
        return arr
                
        