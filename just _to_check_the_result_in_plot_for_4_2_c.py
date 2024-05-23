import matplotlib.pyplot as plt
import pandas as pd

# Data for the final positions and states of the robots
data = [
    {"Robot": 0, "X": 9.87, "Y": 9.39, "Stopped": True},
    {"Robot": 1, "X": 7.93, "Y": 2.65, "Stopped": True},
    {"Robot": 2, "X": 7.20, "Y": 4.64, "Stopped": True},
    {"Robot": 3, "X": 5.79, "Y": 7.05, "Stopped": True},
    {"Robot": 4, "X": 7.26, "Y": 2.80, "Stopped": True},
    {"Robot": 5, "X": 8.63, "Y": 2.70, "Stopped": True},
    {"Robot": 6, "X": 1.23, "Y": 8.47, "Stopped": True},
    {"Robot": 7, "X": 7.76, "Y": 4.79, "Stopped": True},
    {"Robot": 8, "X": 0.63, "Y": 6.46, "Stopped": True},
    {"Robot": 9, "X": 10.00, "Y": 9.18, "Stopped": True},
    {"Robot": 10, "X": 4.35, "Y": 1.98, "Stopped": True},
    {"Robot": 11, "X": 5.35, "Y": 6.28, "Stopped": True},
    {"Robot": 12, "X": 4.08, "Y": 1.52, "Stopped": True},
    {"Robot": 13, "X": 1.54, "Y": 7.67, "Stopped": True},
    {"Robot": 14, "X": 4.43, "Y": 6.60, "Stopped": True},
    {"Robot": 15, "X": 4.46, "Y": 3.88, "Stopped": True},
    {"Robot": 16, "X": 7.89, "Y": 2.09, "Stopped": True},
    {"Robot": 17, "X": 1.23, "Y": 6.76, "Stopped": True},
    {"Robot": 18, "X": 4.58, "Y": 4.23, "Stopped": True},
    {"Robot": 19, "X": 6.97, "Y": 4.30, "Stopped": True},
]

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Visualizing the final positions of the robots
plt.figure(figsize=(10, 8))
for _, row in df.iterrows():
    plt.scatter(row['X'], row['Y'], label=f"Robot {row['Robot']}", marker='o' if row['Stopped'] else 'x')

plt.title("Final Positions of the Robots")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.show()
