class ThroneInheritance:

    def __init__(self, kingName: str):
        self.inheritance = defaultdict(list)
        self.kingName = kingName
        self.deathSet = set()
        

    def birth(self, parentName: str, childName: str) -> None:
        self.inheritance[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.deathSet.add(name)

        

    def getInheritanceOrder(self) -> List[str]:
        inheritanceOrder = []

        def dfs(name):
            for child in self.inheritance[name]:
                if child not in self.deathSet:
                    inheritanceOrder.append(child)
            
                if child in self.inheritance:
                    dfs(child)
        if self.kingName not in self.deathSet:
            inheritanceOrder.append(self.kingName)
            
        dfs(self.kingName)
        return inheritanceOrder

        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
