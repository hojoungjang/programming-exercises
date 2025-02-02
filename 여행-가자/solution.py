import sys
from collections import deque

def solution(graph, travel_plan):
    for i in range(len(travel_plan) - 1):
        # 인덱스 맞추기 위해 -1
        start = travel_plan[i] - 1
        end = travel_plan[i+1] - 1

        queue = deque([start])
        visited = set([start])
        connected = False

        while queue:
            node = queue.popleft()

            if node == end:
                connected = True
                break

            for next_node in range(len(graph[node])):
                if graph[node][next_node] and next_node not in visited:
                    visited.add(next_node)
                    queue.append(next_node)
        
        if not connected:
            return False
    
    return True

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    graph = [[int(val) for val in sys.stdin.readline().strip().split(" ")] for _ in range(n)]
    travel_plan = [int(val) for val in sys.stdin.readline().strip().split(" ")]

    if solution(graph, travel_plan):
        print("YES")
    else:
        print("NO")