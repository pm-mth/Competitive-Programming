class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque([i for i in range(len(tickets))])
        time_taken = 0
        
        while len(queue) > 1:
            time_taken += 1
            index = queue.popleft()
            tickets[index] -= 1
            
            if index == k and tickets[index] == 0:
                return time_taken
            
            if tickets[index]:
                queue.append(index)
        
        return time_taken + tickets[k]
        
        
        