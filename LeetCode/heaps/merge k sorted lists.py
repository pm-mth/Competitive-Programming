# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ascending = []
        dummy = ListNode(0)
        for i in range(len(lists)):
            head = lists[i]
            while head:
                node = head
                head = head.next
                # node.next = None
                heapq.heappush(ascending, node.val)
        node = dummy
        while ascending:
            val = heapq.heappop(ascending)
            newNode = ListNode(val)
            node.next = newNode
            node = newNode
        
        return dummy.next


       
