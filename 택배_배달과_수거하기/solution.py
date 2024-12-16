from math import ceil

def solution(cap, n, deliveries, pickups):
    d_cap = 0
    p_cap = 0
    dist = 0
    
    for i in range(n-1, -1, -1):
        d_boxes = deliveries[i]
        p_boxes = pickups[i]
        
        if d_boxes > d_cap:
            trips = ceil((d_boxes - d_cap) / cap)
            d_cap += trips * cap
            p_cap += trips * cap
            dist += trips * (i+1) * 2
            
        if p_boxes > p_cap:
            trips = ceil((p_boxes - p_cap) / cap)
            d_cap += trips * cap
            p_cap += trips * cap
            dist += trips * (i+1) * 2
            
        d_cap -= d_boxes
        p_cap -= p_boxes
        
    return dist


if __name__ == "__main__":
    print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
