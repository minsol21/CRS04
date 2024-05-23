import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage
import random  # Import the random module

class PotentialField:
    def __init__(self, field_size=(100, 100), alpha=0.1, beta=3, gamma=0.01, max_potential=0.25, num_obstacles=12):
        self.field_size = field_size
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.max_potential = max_potential
        self.num_obstacles = num_obstacles
        self.obstacle_seed = random.randint(0, 1000)  # Generate a random seed for obstacles
        self.field = self.create_potential_field()
        self.add_obstacles()
        self.smooth_field()

    def create_potential_field(self):
        x = np.arange(self.field_size[1])
        y = np.arange(self.field_size[0])
        X, Y = np.meshgrid(x, y)
        P = self.max_potential * (
            np.exp(-self.alpha * X) +
            self.beta / (Y + 1000) +
            self.beta / (self.field_size[0] - Y + 1) +
            self.gamma * Y
        )
        return np.clip(P, 0, self.max_potential)

    def add_obstacles(self):
        np.random.seed(self.obstacle_seed)
        for _ in range(self.num_obstacles):
            self.add_obstacle()

    def add_obstacle(self):
        obstacle_center = np.random.randint(0, self.field_size[0], size=2)
        obstacle_radius = np.random.randint(5, 10)
        obstacle_height = self.max_potential

        rr, cc = np.ogrid[:self.field_size[0], :self.field_size[1]]
        distance = np.sqrt((rr - obstacle_center[0])**2 + (cc - obstacle_center[1])**2)
        mask = distance <= obstacle_radius
        self.field[mask] = np.clip(self.field[mask] + obstacle_height * (1 - distance[mask] / obstacle_radius), 0, self.max_potential)

    def smooth_field(self):
        self.field = scipy.ndimage.gaussian_filter(self.field, sigma=1)

    def visualize(self):
        plt.figure(figsize=(10, 8))
        plt.imshow(self.field, cmap='viridis', origin='lower')
        plt.colorbar(label='Potential')
        plt.title('Potential Field with Combined Function and Borders')
        plt.show()

    def get_potential(self, x, y):
        return self.field[y, x]

    def compute_gradient(self):
        grad_y, grad_x = np.gradient(self.field)  # Gradient of the field
        return grad_x, grad_y
