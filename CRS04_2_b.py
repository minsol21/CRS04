import random
import math
import matplotlib.pyplot as plt

class SwarmRobot:
    def __init__(self, pos_x, pos_y, max_wait_time=5):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = random.uniform(-1, 1)  # starting velocity in x direction
        self.vel_y = random.uniform(-1, 1)  # starting velocity in y direction
        self.is_stopped = False
        self.stop_time = 0
        self.max_wait_time = max_wait_time
    
    def update_position(self):
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
            self.check_boundaries()
    
    def check_boundaries(self, arena_size=10):
        if self.pos_x < 0: self.pos_x = 0
        if self.pos_x > arena_size: self.pos_x = arena_size
        if self.pos_y < 0: self.pos_y = 0
        if self.pos_y > arena_size: self.pos_y = arena_size
    
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

# initialize the arena with 20 swarm robots
arena_dimension = 10
number_of_robots = 20
swarm = [SwarmRobot(random.uniform(0, arena_dimension), random.uniform(0, arena_dimension)) for _ in range(number_of_robots)]

# simulation loop for 100 steps with visualization
for step in range(100):
    plt.clf()  # Clear the previous plot
    plt.xlim(0, arena_dimension)
    plt.ylim(0, arena_dimension)
    plt.title(f"Step {step}")
    plt.xlabel("X position")
    plt.ylabel("Y position")
    
    for robot in swarm:
        robot.check_proximity_and_halt(swarm)
    for robot in swarm:
        robot.update_position()
        color = 'red' if robot.is_stopped else 'blue'
        plt.scatter(robot.pos_x, robot.pos_y, c=color)

    plt.pause(0.1)  # pause to update the plot

plt.show()

# output the final positions and states of the swarm robots
print("\nFinal positions and states of the swarm robots:")
for index, robot in enumerate(swarm):
    print(f"Robot {index}: Position ({robot.pos_x:.2f}, {robot.pos_y:.2f}), Stopped: {robot.is_stopped}, Stop Time: {robot.stop_time}")
