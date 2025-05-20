import sys

def solution(points, reg_info, bettings):
    min_pts_req = []
    for (applied, max_cap), betting_list in zip(reg_info, bettings):
        if max_cap > applied:
            pts_req = 1
        else:
            pts_req = sorted(betting_list, reverse=True)[max_cap-1]
        
        min_pts_req.append(pts_req)
    
    cnt = 0
    for pts_req in sorted(min_pts_req):
        if points < pts_req:
            break
        points -= pts_req
        cnt += 1
    return cnt

if __name__ == "__main__":
    n, points = map(int, sys.stdin.readline().strip().split(" "))

    reg_info = []
    bettings = []
    for _ in range(n):
        applied, max_cap = map(int, sys.stdin.readline().strip().split(" "))
        reg_info.append((applied, max_cap))
        bettings.append([int(val) for val in sys.stdin.readline().strip().split(" ")])

    print(solution(points, reg_info, bettings))

