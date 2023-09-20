import traci
import traci.constants as tc
import math
import csv

# Define your SUMO file paths
sumo_binary = "C:\\Program Files (x86)\\Sumo\\bin\\sumo.exe"
sumo_config = "D:\\ASTGCN-master\\data\\gunes_kcetas\\gunes_kcetas\\gunes_kcetas_morning.sumocfg"
net_file = "D:\\ASTGCN-master\\data\\gunes_kcetas\\gunes_kcetas\\gunes_kcetas.net.xml"

# Initialize TraCI
traci.start([sumo_binary, "-c", sumo_config])

# Get a list of all junction IDs in the simulation
junction_ids = traci.junction.getIDList()

# Function to calculate the distance between two points
def euclidean_distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# List to store distance data
distance_data = []

# Iterate through all junctions and calculate distances to other junctions
for junction_id1 in junction_ids:
    for junction_id2 in junction_ids:
        if junction_id1 != junction_id2:
            # Get coordinates of both junctions
            coords1 = traci.junction.getPosition(junction_id1)
            coords2 = traci.junction.getPosition(junction_id2)
            
            # Calculate the distance between the junctions
            distance = euclidean_distance(coords1, coords2)
            
            # Append the data to the list
            distance_data.append((junction_id1, junction_id2, 1 / distance))

# Write data to CSV file
with open('graph.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['id1', 'id2', '1/distance'])
    csv_writer.writerows(distance_data)

# Close TraCI connection
traci.close()
