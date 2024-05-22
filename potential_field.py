import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage

# Define the size of the potential field
field_size = (100, 100)

# Parameters for the potential field
alpha = 0.1  # Increased for steeper decay from left
beta = 3  # Increased for steeper decay from top and bottom
max_potential = 0.25

# Create the potential field
x = np.arange(field_size[1])
y = np.arange(field_size[0])
X, Y = np.meshgrid(x, y)

# Calculate the potential field using the combined function
P = max_potential * (np.exp(-alpha * X) + beta / (Y + 1) + beta / (field_size[0] - Y + 1))

# Normalize the potential field to ensure values are between 0 and 0.25
P = np.clip(P, 0, max_potential)

# Add obstacles (local maxima)
num_obstacles = 12
np.random.seed(42)  # For reproducibility

for _ in range(num_obstacles):
    obstacle_center = np.random.randint(0, field_size[0], size=2)
    obstacle_radius = np.random.randint(5, 10)
    obstacle_height = max_potential  # Set obstacle height to maximum

    rr, cc = np.ogrid[:field_size[0], :field_size[1]]
    distance = np.sqrt((rr - obstacle_center[0])**2 + (cc - obstacle_center[1])**2)
    mask = distance <= obstacle_radius
    P[mask] = np.clip(P[mask] + obstacle_height * (1 - distance[mask] / obstacle_radius), 0, max_potential)

# Ensure the final potential field is within the range [0, 0.25]
P = np.clip(P, 0, max_potential)

# Smooth the potential field to make the obstacles more natural (optional)
P = scipy.ndimage.gaussian_filter(P, sigma=1)

# Visualize the potential field
plt.figure(figsize=(10, 8))
plt.imshow(P, cmap='viridis', origin='lower')
plt.colorbar(label='Potential')
plt.title('Potential Field with Combined Function and Borders')
plt.show()
