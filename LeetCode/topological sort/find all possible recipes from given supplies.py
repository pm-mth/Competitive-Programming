class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        recipe_set = set(recipes)
        supply = [0] * len(recipes)
        supplies_set = set(supplies)
        queue = deque()

        order = []

        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                if ingredients[i][j] in recipe_set:
                    graph[ingredients[i][j]].append((recipes[i], i))
                    in_degree[recipes[i]] += 1
                    supply[i] += 1
                if ingredients[i][j] in supplies_set:
                    supply[i] += 1
        
        for i in range(len(recipes)):
            if in_degree[recipes[i]] == 0 and supply[i] == len(ingredients[i]):
                queue.append(recipes[i])
        
        while queue:
            recipe = queue.popleft()
            order.append(recipe)

            for neighbor, idx in graph[recipe]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0 and supply[idx] == len(ingredients[idx]):
                    queue.append((neighbor))
    
        
        return order
