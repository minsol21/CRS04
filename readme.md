# Project Directory: CRS04_01

This project contains implementations for CRS04 assignment. The project directory is organized as follows:

## Directory Structure

project_directory/
├── CRS04_01
│ ├── PotentialField.py
│ ├── RobotMovement.py
│ ├── RobotMovement2.py
│ └── main.py
├── CRS04_02_a
├── CRS04_02_b
├── CRS04_02_c
└── README.md


## File Descriptions

### CRS04_01

- **PotentialField.py**: 
  - Contains the `PotentialField` class, which generates a potential field with specified parameters. The field includes a gradient in both the x and y directions, and randomly placed obstacles.
  - Key methods:
    - `__init__`: Initializes the potential field.
    - `create_potential_field`: Creates the potential field with the specified gradient.
    - `add_obstacles`: Adds obstacles to the potential field.
    - `smooth_field`: Smooths the field to make the obstacles more natural.
    - `visualize`: Visualizes the potential field.
    - `get_potential`: Returns the potential value at a specific location.
    - `compute_gradient`: Computes the gradient of the potential field.

- **RobotMovement.py**:
  - Represents task a of the CRS04_01 assignment. This file contains the `RobotMovement` class, which generates robot trajectories based on the gradient of the potential field.
  - Key methods:
    - `__init__`: Initializes the robot movement with the potential field.
    - `generate_trajectory`: Generates a trajectory for the robot starting from a given position.
    - `visualize_trajectory`: Visualizes the robot's trajectory on the potential field.

- **RobotMovement2.py**:
  - Represents task b of the CRS04_01 assignment. This file contains the `RobotMovement2` class, which implements a different algorithm or approach to generate robot trajectories.
  - Key methods:
    - `__init__`: Initializes the robot movement with the potential field.
    - `generate_trajectory_b`: Generates a trajectory for the robot using a different algorithm (specific to task b).
    - `visualize_trajectory`: Visualizes the robot's trajectory on the potential field.

- **main.py**:
  - Main script to run and test the implementations in `RobotMovement.py`.
  - Key functions:
    - `main`: Main function to create instances of `PotentialField`, `RobotMovement`generate trajectories, and visualize the results.

### CRS04_02_a, CRS04_02_b, CRS04_02_c

- These directories are placeholders for additional tasks or parts of the CRS04 assignment series. Each directory may contain its own set of scripts and data relevant to its specific task.

## Usage

To run the main script and visualize the robot trajectories for task a and task b:
Ensure you have the necessary dependencies installed:
   ```bash
   pip install numpy matplotlib scipy
