from collections import deque

SHEEP = 0
WOLF = 1

def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for u, v in edges:
        graph[u].append(v)
    
    queue = deque()
    queue.append((0, 1, 0, list(graph[0])))
    max_sheep = 0
    
    while queue:
        
        node, sheep, wolf, next_nodes = queue.popleft()
        max_sheep = max(max_sheep, sheep)
        
        for next_node in next_nodes:
            next_sheep = sheep
            next_wolf = wolf
            next_next_nodes = list(next_nodes)
            
            if info[next_node] == SHEEP:
                next_sheep += 1
            else:
                next_wolf += 1
                
            if next_sheep <= next_wolf:
                continue
                
            next_next_nodes.remove(next_node)
            for child_node in graph[next_node]:
                next_next_nodes.append(child_node)
                
            queue.append((next_node, next_sheep, next_wolf, next_next_nodes))
                
    return max_sheep
