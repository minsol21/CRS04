import random
import math

class SwarmRobot:
    def __init__(self, pos_x, pos_y, max_wait_time=5):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = random.uniform(-1, 1)  # strating velocity in x direction
        self.vel_y = random.uniform(-1, 1)  # starting velocity in y direction
        self.is_stopped = False
        self.stop_time = 0
        self.max_wait_time = max_wait_time
    
    def update_Position(self):
        if self.is_stopped:
            self.stop_time += 1
            if self.stop_time >= self.max_wait_time:
                self.is_stopped = False
                self.stop_time = 0
                self.vel_x = random.uniform(-1, 1)
                self.vel_y = random.uniform(-1, 1)
        if not self.is_stopped:
            self.pos_x += self.vel_x
            self.pos_y += self.vel_y
    
    def calculate_distance(self, other_robot):
        return math.sqrt((self.pos_x - other_robot.pos_x) ** 2 + (self.pos_y - other_robot.pos_y) ** 2)
    
    def check_proximity_and_halt(self, swarm, stop_distance=1.0):
        if not self.is_stopped:
            for other_robot in swarm:
                if other_robot != self and self.calculate_distance(other_robot) < stop_distance:
                    self.is_stopped = True
                    self.vel_x = 0
                    self.vel_y = 0
                    break

# Initialize the arena with 20 swarm robots
arena_dimension = 10
number_of_robots = 20
swarm = [SwarmRobot(random.uniform(0, arena_dimension), random.uniform(0, arena_dimension)) for _ in range(number_of_robots)]

# Simulation loop for 100 steps
for step in range(100):
    for robot in swarm:
        robot.check_proximity_and_halt(swarm)
    for robot in swarm:
        robot.update_Position()

# Output the final positions and states of the swarm robots
for index, robot in enumerate(swarm):
    print(f"Robot {index}: Position ({robot.pos_x}, {robot.pos_y}), Stopped: {robot.is_stopped}, Stop Time: {robot.stop_time}")

# A robot stops for a defined waiting time whn it gets too close to another robot.
# After a waiting period, it resumes moving anf stopping again if it encounters another robot.
# this helps in breaking up clusters and making swarm's dynmaic behavior