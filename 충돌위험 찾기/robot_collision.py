from typing import List
from collections import Counter

class Robot:
    def __init__(self, route_coords, start_coord, robot_id):
        self.robot_id = robot_id
        self.route = route_coords
        self.route_idx = 0
        self.pos = start_coord      # Must be tuple
        self.complete = False
        
    def __repr__(self):
        return f"<ID: {self.robot_id} pos: {self.pos} dest: {self.route[self.route_idx]}>"
        
    def move(self):
        if self.route[self.route_idx] == self.pos:
            if self.route_idx + 1 == len(self.route):
                self.complete = True
                return
            self.route_idx += 1

        dest_coord = self.route[self.route_idx]

        row_delta = dest_coord[0] - self.pos[0]
        col_delta = dest_coord[1] - self.pos[1]
        
        if row_delta != 0:
            new_row = self.pos[0] + (row_delta // abs(row_delta))
            self.pos = (new_row, self.pos[1],)
            return
    
        if col_delta != 0:
            new_col = self.pos[1] + (col_delta // abs(col_delta))
            self.pos = (self.pos[0], new_col,)


def solution(points, routes):
    points = [[-1,-1]] + points # add dummy for intuitive indexing
    robots = [
        Robot(
            route_coords=[tuple(points[p_idx]) for p_idx in route],
            start_coord=tuple(points[route[0]]),
            robot_id=i+1,
        ) for i, route in enumerate(routes) if route
    ]
    
    start_pos_counts = Counter(robot.pos for robot in robots)
    collision = len([cnt for cnt in start_pos_counts.values() if cnt > 1])

    while not all(robot.complete for robot in robots):
        for robot in robots:
            print(robot)
        print()

        for robot in robots:
            if robot.complete:
                continue
            robot.move()
            
        pos_counts = Counter(robot.pos for robot in robots if not robot.complete)
        collision += len([cnt for cnt in pos_counts.values() if cnt > 1])
        
    return collision


if __name__ == "__main__":
    points = [[3, 2], [6, 4], [4, 7], [1, 4]]
    routes = [[4, 2], [1, 3], [2, 4]]
    print(solution(points, routes))

    points = [[3, 2], [6, 4], [4, 7], [1, 4]]
    routes = [[4, 2], [1, 3], [4, 2], [4, 3]]
    print(solution(points, routes))

    points = [[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]]
    routes = [[2, 3, 4, 5], [1, 3, 4, 5]]
    print(solution(points, routes))


