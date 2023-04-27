class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set([0])
        queue = deque([0])

        count = len(rooms) - 1

        while queue:
            index = queue.popleft()

            for idx in rooms[index]:
                if idx not in visited:
                    visited.add(idx)
                    queue.append(idx)
                    count -= 1
                    
        return True if not count else False

