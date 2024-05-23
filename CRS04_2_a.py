import random
import math

class SwarmRobot:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = random.uniform(-1, 1)  # starting velocity in x direction
        self.vel_y = random.uniform(-1, 1)  # starting velocity in y direction
        self.is_stopped = False
    
    def update_position(self, arena_dimension):
        if not self.is_stopped:
            self.pos_x += self.vel_x
            self.pos_y += self.vel_y

            # ensure the robot stays within the arena boundaries
            if self.pos_x <= 0 or self.pos_x >= arena_dimension:
                self.vel_x *= -1  # reverse direction on x-axis boundary collision

            if self.pos_y <= 0 or self.pos_y >= arena_dimension:
                self.vel_y *= -1  # reverse direction on y-axis boundary collision

            self.pos_x = min(max(self.pos_x, 0), arena_dimension)
            self.pos_y = min(max(self.pos_y, 0), arena_dimension)
    
    def calculate_distance(self, other_robot):
        return math.sqrt((self.pos_x - other_robot.pos_x) ** 2 + (self.pos_y - other_robot.pos_y) ** 2)
    
    def check_proximity_and_halt(self, swarm, stop_distance=1.0):
        for other_robot in swarm:
            if other_robot != self and self.calculate_distance(other_robot) < stop_distance:
                self.is_stopped = True
                self.vel_x = 0
                self.vel_y = 0
                break

# initialize the arena with 20 swarm robots
arena_dimension = 10
number_of_robots = 20
swarm = [SwarmRobot(random.uniform(1, arena_dimension - 1), random.uniform(1, arena_dimension - 1)) for _ in range(number_of_robots)]

# simulation loop for 100 steps
for step in range(100):
    for robot in swarm:
        robot.check_proximity_and_halt(swarm)
    for robot in swarm:
        robot.update_position(arena_dimension)
    # output positions and states at each step
    print(f"Step {step + 1}:")
    for index, robot in enumerate(swarm):
        print(f"  Robot {index}: Position ({robot.pos_x:.2f}, {robot.pos_y:.2f}), Stopped: {robot.is_stopped}")

# final output of the positions and states of the swarm robots
print("\nFinal positions and states of the swarm robots:")
for index, robot in enumerate(swarm):
    print(f"Robot {index}: Position ({robot.pos_x:.2f}, {robot.pos_y:.2f}), Stopped: {robot.is_stopped}")
