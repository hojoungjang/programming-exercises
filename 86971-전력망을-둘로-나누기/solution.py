"""
프로그래머스
전력망을 둘로 나누기
https://school.programmers.co.kr/learn/courses/30/lessons/86971
"""
def solution(n, wires):
    
    def dfs(node):
        visited.add(node)
        count = 1
        for next_node in graph[node]:
            if (node == removed[0] and next_node == removed[1]) or (node == removed[1] and next_node == removed[0]):
                continue
            if next_node in visited:
                continue
            count += dfs(next_node)
        return count

    graph = [[] for _ in range(n+1)]
    for u, v in wires:
        graph[u].append(v)
        graph[v].append(u)
    
    min_diff = float("inf")
    
    for node in range(1, n+1):
        for next_node in graph[node]:
            removed = (node, next_node)
            visited = set()
            count1 = dfs(node)
            count2 = dfs(next_node)
            min_diff = min(min_diff, abs(count1 - count2))
    
    return min_diff
