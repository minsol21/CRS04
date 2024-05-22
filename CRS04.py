import numpy as np
import matplotlib.pyplot as plt
import random

# Parameters
width, height = 100, 100
n_obstacles = 8
robot_start_width = 10  # Robot starts within the first 10 columns

# Create the potential field with a basic linear gradient and boundary influence
x = np.linspace(0, 1, width)
y = np.linspace(0, 1, height)
X, Y = np.meshgrid(x, y)

P = 0.25 * (1-X)  # Decrease from left to right, and slope away from edges
#P = 0.25 * (np.maximum(X, 1 - X) + np.maximum(Y, 1 - Y))
# Create the potential field with high potential at borders
#P = 0.25 * (np.maximum(X, 1 - X) + np.maximum(Y, 1 - Y))

# Add Gaussian obstacles randomly
for _ in range(n_obstacles):
    center_x = random.randint(0, width-1)
    center_y = random.randint(0, height-1)
    radius = random.uniform(5, 10)  # Radius of the obstacle's effect
    obstacle_height = 0.25 * (random.uniform(0.2, 0.4))  # Height of the obstacle's peak effect
    
    for i in range(height):
        for j in range(width):
            distance = np.sqrt((center_x - j)**2 + (center_y - i)**2)
            P[i, j] += obstacle_height * np.exp(-(distance**2) / (2 * radius**2))

# Normalize the potential field to be between 0 and 1
#P_min = np.min(P)
#P_max = np.max(P)
#P_normalized = (P - P_min) / (P_max - P_min)

# Normalize the potential field so that the maximum is 0.25
#P_max = np.max(P)
#P_normalized = (P / P_max) * 0.25

# Place the robot
robot_x = random.randint(0, robot_start_width-1)
robot_y = random.randint(0, height-1)
robot_position = (robot_x, robot_y)



# Visualize the field and robot position
plt.figure(figsize=(10, 10))
plt.imshow(P, origin='lower', cmap='plasma')
plt.colorbar(label='Potential')
plt.scatter(*robot_position, color='red')  # Show the robot's position
plt.title('Potential Field with Obstacles and Robot Position')
plt.show()
