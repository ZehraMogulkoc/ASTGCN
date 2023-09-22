import numpy as np

# Load the NPZ file
data = np.load('D:\\ASTGCN-master\\data\\PEMS04\\gunes_kcetas_c2.npz')

# Get the list of keys (file names)
lst = data.files

# Print the number of files
num_files = len(lst)
print("Number of files in the NPZ archive:", num_files)

# Print the names of the files (keys) and their corresponding shapes
for key in lst:
    data_shape = data[key].shape
    print(f"File name: {key}, Data shape: {data_shape}")


traffic_data = data[lst[0]]
data_dict = []
# loop for every timestep and every location and add as a single row


print(data[lst[0]].shape)
print(data[lst[0]])
#for item in data[lst[0]]:
 #   print(item)