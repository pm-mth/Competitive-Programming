class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1

        queue = deque()
        queue.append([[0,0,0,0], 0])
        visited = set("0000")

        while queue:
            wheels, d = queue.popleft()
            lock = "".join(map(str, wheels))
            if target == lock:
                return d

            for i in range(len(wheels)):
                add = wheels[i] + 1
                sub = wheels[i] - 1
                if add == 10:
                    add = 0
                if sub == -1:
                    sub = 9
                
                inc = wheels.copy()
                inc[i] = add
                dec = wheels.copy()
                dec[i] = sub

                check = "".join(map(str, dec))

                if check not in deadends and check not in visited:
                    queue.append([dec, d + 1])
                    visited.add(check)
                check = "".join(map(str, inc))
                if check not in deadends and check not in visited:
                    queue.append([inc, d + 1])
                    visited.add(check)
        return - 1

