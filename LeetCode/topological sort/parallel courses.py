from collections import defaultdict, deque
def parallelCourses(n, prerequisites):
    # Write your code here.
    graph = defaultdict(list)
    degree = defaultdict(int)
  
        
    for pre, suf in prerequisites:
        graph[pre].append(suf)
        degree[suf] += 1
        
    queue = deque()
        
    courses = 0
    for i in range(1, n + 1):
        if degree[i] == 0:
            courses += 1
            queue.append(i)
  
  
    semster = 0
    while queue:
        semster += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            for neighbour in graph[node]:
                degree[neighbour] -= 1
                if degree[neighbour] == 0:
                    courses += 1
                    queue.append(neighbour)
        
    if courses == n:
        return semster
    return -1


    pass
