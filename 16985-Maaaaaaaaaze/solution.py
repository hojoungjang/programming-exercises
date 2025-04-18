"""
백준
Maaaaaaaaaze
https://www.acmicpc.net/problem/16985
"""

import sys
from itertools import product, permutations
from collections import deque

NUMBER_OF_PLATES = 5
PLATE_SIZE = 5
NUMBER_OF_ROTATIONS = 4
MAX_PATH_LENGTH = (PLATE_SIZE ** 2) * NUMBER_OF_PLATES

INVALID_BLOCK = 0
VALID_BLOCK = 1

START_END = [
    ((0, 0, 0), (4, 4, 4)),
    ((0, 4, 0), (4, 0, 4)),
    ((4, 0, 0), (0, 4, 4)),
    ((4, 4, 0), (0, 0, 4)),
]

def get_rotation(plate):
    rot = [
        [[val for val in row] for row in plate]
    ]
    for _ in range(NUMBER_OF_ROTATIONS-1):
        new_plate = [[val for val in row] for row in rot[-1]]
        for i in range(PLATE_SIZE // 2 + 1):
            last = PLATE_SIZE - i - 1
            for jidx, j in enumerate(range(i, last)):
                new_plate[i][j], new_plate[j][last], new_plate[last][last-jidx], new_plate[last-jidx][i] = new_plate[last-jidx][i], new_plate[i][j], new_plate[j][last], new_plate[last][last-jidx]

        rot.append(new_plate)
    return rot


def find_way_out(maze):
    shortest_path = MAX_PATH_LENGTH + 1

    for start, end in START_END:
        sr, sc, sd = start
        er, ec, ed = end

        if maze[sr][sc][sd] == INVALID_BLOCK or maze[er][ec][ed] == INVALID_BLOCK:
            continue

        queue = deque([start, None])
        visited = set([start])
        path_cnt = 0

        while queue:
            # next level
            if queue[0] is None:
                queue.popleft()
                if queue:
                    queue.append(None)
                
                path_cnt += 1
                if path_cnt >= shortest_path:
                    break
                else:
                    continue

            r, c, d = queue.popleft()

            if (r, c, d) == end:
                shortest_path = min(shortest_path, path_cnt)
                break

            for dr, dc, dd in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
                new_r = r + dr
                new_c = c + dc
                new_d = d + dd

                if new_r < 0 or new_r >= PLATE_SIZE:
                    continue
                if new_c < 0 or new_c >= PLATE_SIZE:
                    continue
                if new_d < 0 or new_d >= PLATE_SIZE:
                    continue

                if (new_r, new_c, new_d) in visited:
                    continue

                if maze[new_r][new_c][new_d] == INVALID_BLOCK:
                    continue

                visited.add((new_r, new_c, new_d))
                queue.append((new_r, new_c, new_d))

    return shortest_path if shortest_path < MAX_PATH_LENGTH + 1 else -1

def solution(plates):
    """
    each plate has 4 ways
    there are 5 plates
    plates can be rearraged

    4 * 4 * 4 * 4 * 4
    4^5 * 5!

    for each maze has 4 path ways (i.e. start and end combination)
    for each way at most 125 iterations
    """
    plate_rots = []
    for plate in plates:
        plate_rots.append(get_rotation(plate))

    shortest_path = MAX_PATH_LENGTH + 1
    dup_maze = set()

    for plate_order in permutations(range(NUMBER_OF_PLATES)):
        for rotation_indices in product(range(NUMBER_OF_ROTATIONS), repeat=NUMBER_OF_PLATES):
            maze = []
            for pidx, ridx in zip(plate_order, rotation_indices):
                maze.append(plate_rots[pidx][ridx])
            
            if (str_maze := str(maze)) not in dup_maze:
                dup_maze.add(str_maze)
                path_cnt = find_way_out(maze)
                if path_cnt != -1:
                    shortest_path = min(shortest_path, path_cnt)
                    if shortest_path == 12:
                        return shortest_path
    
    return shortest_path if shortest_path < MAX_PATH_LENGTH + 1 else -1


if __name__ == "__main__":
    plates = []
    for _ in range(NUMBER_OF_PLATES):
        plate = []
        for _ in range(PLATE_SIZE):
            plate.append(tuple(int(val) for val in sys.stdin.readline().strip().split(" ")))
        plates.append(plate)
    print(solution(plates))