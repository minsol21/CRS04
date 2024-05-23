from CRS04_01.PotentialField import PotentialField
from CRS04_01.RobotMovement import RobotMovement

def main():
    # Create an instance of PotentialField
    potential_field = PotentialField()

    # Visualize the potential field
    #potential_field.visualize()

    # Set the starting position, number of steps, and integration step size
    start_position = (10, 50)  # Starting position of the robot
    num_steps = 100000  # Number of steps to simulate
    dt = 100  # Integration step size

    # Create an instance of RobotMovement with the potential field
    robot_movement = RobotMovement(potential_field)

    # Generate the trajectory
    trajectory = robot_movement.generate_trajectory(start_position, num_steps, dt)

    # Visualize the trajectory on the potential field
    robot_movement.visualize_trajectory(trajectory)

if __name__ == "__main__":
    main()
