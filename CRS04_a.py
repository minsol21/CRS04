import numpy as np
import matplotlib.pyplot as plt
import random

# Parameters
width, height = 100, 100
n_obstacles = 8
delta_t = 0.1  # Time step for integration
robot_start_width = 10  # Robot starts within the first 10 columns

n_steps = 500  # Number of steps to simulate
scale_velocity = 5  # Scaling factor for velocity to adjust the motion speed


# Create the potential field with a basic linear gradient and boundary influence
x = np.linspace(0, 1, width)
y = np.linspace(0, 1, height)
X, Y = np.meshgrid(x, y)
P = (1 - X) + (0.5 - abs(0.5 - Y)) * 0.2  # Decrease from left to right, and slope away from edges

# Add Gaussian obstacles randomly
for _ in range(n_obstacles):
    center_x = random.randint(0, width-1)
    center_y = random.randint(0, height-1)
    radius = random.uniform(5, 15)  # Radius of the obstacle's effect
    obstacle_height = random.uniform(40, 80)  # Height of the obstacle's peak effect
    for i in range(height):
        for j in range(width):
            distance = np.sqrt((center_x - j)**2 + (center_y - i)**2)
            P[i, j] += obstacle_height * np.exp(-(distance**2) / (2 * radius**2))

# Normalize the potential field to be between 0 and 1
P_min = np.min(P)
P_max = np.max(P)
P_normalized = (P - P_min) / (P_max - P_min)


# Place the robot
robot_x = random.randint(0, robot_start_width-1)
robot_y = random.randint(0, height-1)
robot_position = np.array([robot_x, robot_y], dtype=float)
trajectory = [robot_position.copy()]


for _ in range(n_steps):
    i, j = int(robot_position[0]), int(robot_position[1])  # Convert position to integer for indexing
    # Calculate gradient
    if i < width - 1:
        vx = P[j, i] - P[j, i + 1]
    else:
        vx = 0  # No gradient if on the last column
    if j < height - 1:
        vy = P[j, i] - P[j + 1, i]
    else:
        vy = 0  # No gradient if on the last row


    # Update robot position
    robot_position += np.array([vx, vy]) * delta_t * scale_velocity
    trajectory.append(robot_position.copy())

trajectory = np.array(trajectory)




# Visualize the field and robot position
plt.figure(figsize=(10, 10))
plt.imshow(P, origin='lower', cmap='plasma', extent=[0, width, 0, height])
plt.colorbar(label='Potential')
plt.plot(trajectory[:, 0], trajectory[:, 1], 'w.-')  # White line for trajectory
#plt.scatter(*robot_position, color='red')  # Show the robot's position
plt.scatter(trajectory[0, 0], trajectory[0, 1], color='blue')  # Start position
plt.scatter(trajectory[-1, 0], trajectory[-1, 1], color='red')  # End position
plt.title('Robot Trajectory on Potential Field')
plt.title('Potential Field with Obstacles and Robot Position')
plt.show()
