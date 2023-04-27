class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.graph = defaultdict(list)
        for i in range(len(parent)):
            self.graph[parent[i]].append(i)

        self.locked = defaultdict(int)
        

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
            
        self.locked[num] = user
        return True
        

    def unlock(self, num: int, user: int) -> bool:
        if num not in self.locked:
            return False

        if self.locked[num] == user:
            del self.locked[num]
            return True
        
        return False
        

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        
        visited = set()
        def ancestor(num):
            nonlocal visited
            if num == -1:
                return True

            if num in self.locked:
                return False
            

            if num not in visited:
                visited.add(num)
                return ancestor(self.parent[num])
        if not ancestor(num):
            return False
     
        flag = False
        visited = set([num])
        def descendant(num):
            nonlocal flag
            nonlocal visited

            if num in self.locked:
                flag = True
                del self.locked[num]
            
            for node in self.graph[num]:
                if node not in visited:
                    visited.add(node)
                    descendant(node)
        descendant(num)
        if not flag:
            return False

        self.locked[num] = user
        return True
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
