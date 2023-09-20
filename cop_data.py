import xml.etree.ElementTree as ET
import copy

# Load the XML file
input_file = r'D:\\ASTGCN-master\\data\\gunes_kcetas\\gunes_kcetas\\gunes_kcetas_morning.rou.xml'
tree = ET.parse(input_file)
root = tree.getroot()

# Find all vehicle elements
vehicles = root.findall('.//vehicle')

# Create a set to store existing IDs
existing_ids = set()

# Extract existing IDs from the data
for vehicle in vehicles:
    id_value = int(vehicle.get('id'))
    existing_ids.add(id_value)

# Create a list to store the duplicated vehicle elements
duplicated_vehicles = []

# Find the maximum existing ID
max_existing_id = max(existing_ids)

# Duplicate and increment the 'id' attribute for each vehicle
for vehicle in vehicles:
    id_value = int(vehicle.get('id'))
    # Clone the vehicle element
    new_vehicle = copy.deepcopy(vehicle)
    # Increment the 'id' attribute for the clone
    max_existing_id += 1
    new_vehicle.set('id', str(max_existing_id))
    # Append the cloned element to the list
   
    duplicated_vehicles.append(new_vehicle)

print(len(duplicated_vehicles))

# Append the duplicated vehicle elements to the root
for vehicle in duplicated_vehicles:
    root.append(vehicle)

# Save the modified XML to a new file
output_file = r'D:\\ASTGCN-master\\data\\gunes_kcetas\\gunes_kcetas\\gunes_kcetas_morning_second.rou.xml'
tree.write(output_file)

print(f"Modified XML saved to '{output_file}'")
