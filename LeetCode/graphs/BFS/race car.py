class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0,1, 0)])
        visited = set([(0, 1)])
     

        while queue:
            p, s, d = queue.popleft()
            if p == target:
                return d
            np, ns = p + s, s * 2
            if (np, ns) not in visited:
                visited.add((np, ns))
                queue.append((np, ns, d + 1))
            if s >  0:
                np, ns = p, -1
                if (np, ns) not in visited:
                    visited.add((np, ns))
                    queue.append((np, ns, d + 1))
            else:
                np, ns = p, 1
                if (np, ns) not in visited:
                    visited.add((np, ns))
                    queue.append((np, ns, d + 1))
            
            
