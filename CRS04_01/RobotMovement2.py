import numpy as np
import matplotlib.pyplot as plt
from PotentialField import PotentialField

class RobotMovement2:
    def __init__(self, potential_field: PotentialField):
        self.potential_field = potential_field

    def generate_trajectory(self, start_pos, num_steps, dt,c=0.1):
        trajectory = [start_pos]
        grad_x, grad_y = self.potential_field.compute_gradient()

        x, y = start_pos
        #new_x, new_y = x,y
        velocity = np.array([0.0, 0.0])
        
        for step in range(num_steps):
            x, y = int(round(x)), int(round(y))
            acceleration = np.array([grad_x[y, x], grad_y[y, x]])
            velocity = c * velocity + acceleration
            velocity /= np.linalg.norm(velocity)  # Normalize velocity

            new_x = x + velocity[0] * dt
            new_y = y + velocity[1] * dt
            trajectory.append((new_x, new_y))

            # Stop if the trajectory has converged
            if (int(round(new_x)), int(round(new_y))) == (x, y):
                print(f'Trajectory converged at step {step}')
                break  

        return trajectory

    def visualize_trajectory(self, trajectory):
        plt.figure(figsize=(10, 8))
        plt.imshow(self.potential_field.field, cmap='viridis', origin='lower')
        plt.colorbar(label='Potential')
        plt.title('Potential Field with Trajectory')
        
        trajectory = np.array(trajectory)
        plt.plot(trajectory[:, 0], trajectory[:, 1], color='red', marker='o')
        print(f'Trajectory [:, 0]: {trajectory[:, 0]} ')
        print(f'Trajectory [:, 1]: {trajectory[:, 1]} ')
        
        plt.show()

# Example usage:
if __name__ == "__main__":
    potential_field = PotentialField()

    start_position = (10, 50)  # Starting position of the robot
    num_steps = 1000 # Number of steps to simulate
    dt = 10  # Integration step size

    robot_movement = RobotMovement2(potential_field)
    trajectory = robot_movement.generate_trajectory(start_position, num_steps, dt)
    robot_movement.visualize_trajectory(trajectory)