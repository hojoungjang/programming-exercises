from collections import defaultdict

def get_adj_list(edges):
    graph = defaultdict(list)
    
    for from_node, to_node in edges:
        graph[from_node].append(to_node)
        
    return graph    


def get_start_node(adj_list):
    nodes_with_ins = set()
    for next_nodes in adj_list.values():
        for next_node in next_nodes:
            nodes_with_ins.add(next_node)

    for node, edges in adj_list.items():
        if node not in nodes_with_ins and len(edges) > 1:
            return node
    return 0


def get_vertice_and_edge_counts(adj_list, node: int, visited: set):
    visited.add(node)
    v_count = 1
    e_count = 0

    if node not in adj_list:
        return v_count, e_count
    
    for next_node in adj_list[node]:
        e_count += 1
        if next_node in visited:
            continue
        sub_counts = get_vertice_and_edge_counts(adj_list, next_node, visited)
        v_count += sub_counts[0]
        e_count += sub_counts[1]
    return v_count, e_count


def solution(edges):
    adj_list = get_adj_list(edges)
    start_node = get_start_node(adj_list)

    donut_count = 0
    stick_count = 0
    eight_count = 0
    
    for next_node in adj_list[start_node]:
        visited = set()
        v_count, e_count = get_vertice_and_edge_counts(adj_list, next_node, visited)
        
        ve_diff = v_count - e_count

        if ve_diff == 0:
            donut_count += 1
        elif ve_diff == 1:
            stick_count += 1
        elif ve_diff == -1:
            eight_count += 1

    return [start_node, donut_count, stick_count, eight_count]


if __name__ == "__main__":
    edges = [[2, 3], [4, 3], [1, 1], [2, 1]]
    
    ans = solution(edges)
