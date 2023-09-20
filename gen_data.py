import numpy as np
import pandas as pd

# Load data from the CSV file
csv_file = 'D:\ASTGCN-master\output.csv'  # Replace with your CSV file path
data = []

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file)

# Assuming the DataFrame has the same structure as created earlier
# Number of unique timesteps and locations
num_timesteps = df['timestep'].nunique()
num_locations = df['location'].nunique()

# Create an empty NumPy array to store the data
traffic_data = np.zeros((num_timesteps, num_locations, 3))  # Assuming 3 columns for flow, occupy, speed

# Fill the NumPy array with data from the DataFrame
for index, row in df.iterrows():
    timestep = int(row['timestep']) - 1
    location = int(row['location'])
    flow = row['flow']
    occupy = row['occupy']
    speed = row['speed']
    traffic_data[timestep, location, 0] = flow
    traffic_data[timestep, location, 1] = occupy
    traffic_data[timestep, location, 2] = speed

# Save the NumPy array as an NPZ file
np.savez("traffic_data.npz", traffic_data=traffic_data)
