import numpy as np
import matplotlib.pyplot as plt
from PotentialField import PotentialField

class RobotMovement:
    def __init__(self, potential_field: PotentialField):
        self.potential_field = potential_field

    def generate_trajectory(self, start_pos, num_steps, dt):
        trajectory = [start_pos]
        grad_x, grad_y = self.potential_field.compute_gradient()

        x, y = start_pos
        new_x, new_y = x,y
        
        for step in range(num_steps):
            x, y = int(round(new_x)), int(round(new_y))
            vx = grad_x[y, x]
            vy = grad_y[y, x]
            print(f'{step}th vx: {vx}')
            print(f'{step}th vy: {vy}')
            
            # Update position
            #x = int(np.clip(x + vx * dt, 0, self.potential_field.field_size[1] - 1))
            #y = int(np.clip(y + vy * dt, 0, self.potential_field.field_size[0] - 1))
            new_x = x + vx * dt
            new_y = y + vy * dt
            trajectory.append((new_x, new_y))

            # Log position updates for debugging
            print(f'{step}th position: ({new_x}, {new_y})')
            
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
    potential_field.visualize()
    
    start_position = (10, 50)  # Starting position of the robot
    num_steps = 100000  # Number of steps to simulate
    dt = 1000  # Integration step size

    robot_movement = RobotMovement(potential_field)
    trajectory = robot_movement.generate_trajectory(start_position, num_steps, dt)
    
    robot_movement.visualize_trajectory(trajectory)
