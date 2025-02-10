import sys
sys.setrecursionlimit(5000)

def solution(graph, questions):

    def dfs(idx, score):
        visited.add(idx)
        count = 1
        for next_idx, next_score in graph[idx].items():
            if next_idx in visited:
                continue
            next_score = min(score, next_score)
            if next_score < min_score:
                continue
            count += dfs(next_idx, next_score)
        return count

    counts = [0 for _ in range(len(questions))]
    for i, (min_score, video_idx) in enumerate(questions):
        visited = set()
        counts[i] = dfs(video_idx, float("inf")) - 1
    return counts


if __name__ == "__main__":
    n, q = map(int, sys.stdin.readline().strip().split(" "))
    graph = {v: {} for v in range(1, n+1)}
    for _ in range(n-1):
        u, v, score = map(int, sys.stdin.readline().strip().split(" "))
        graph[u][v] = score
        graph[v][u] = score
    
    questions = [tuple(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(q)]
    video_counts = solution(graph, questions)
    for count in video_counts:
        print(count)
