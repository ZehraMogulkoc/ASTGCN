import pandas as pd

# Read the original CSV file into a DataFrame
original_df = pd.read_csv('D:\ASTGCN-master\kcetas.csv', delimiter=',')

# Initialize variables
num_duplicates = 4
index = 1
increment_timestep=301

# Create an empty DataFrame to store the duplicated data
duplicated_df = pd.DataFrame()

# Duplicate and modify the data
for _ in range(num_duplicates):
    # Determine the maximum timestep value from the original DataFrame
    max_timestep = original_df['timestep'].max()

    # Add the modified data to the duplicated DataFrame
    duplicated_df = pd.concat([duplicated_df, original_df.copy()])
    # Increment the timestep based on the maximum value
    original_df['timestep'] = max_timestep + (increment_timestep * index)

    # Reset index to 1 and increment timestep when all locations have been processed
    if original_df['location'].max() == 20:
        index = 1
        #original_df['timestep'] += increment_timestep

    else:
        index += 1

# Save the duplicated data to a new CSV file
duplicated_df.to_csv('duplicated_data.csv', index=False, sep=',')