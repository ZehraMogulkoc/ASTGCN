import xml.etree.ElementTree as ET
import copy

# Load the XML file
input_file = r'D:\\ASTGCN-master\\data\\gunes_kcetas\\gunes_kcetas\\gunes_kcetas_morning.rou.xml'
tree = ET.parse(input_file)
root = tree.getroot()

# Find all vehicle elements
vehicles = root.findall('.//vehicle')

# Create a list to store the duplicated vehicle elements
duplicated_vehicles = []

# Find the maximum existing ID
max_existing_id = int(max(vehicles, key=lambda vehicle: int(vehicle.get('id'))).get('id'))

# Find the last departure time
last_departure_time = float(vehicles[-1].get('depart'))

# Duplicate each vehicle and increment the 'id' and departure time 30 times
for _ in range(30):
    for vehicle in vehicles:
        # Clone the vehicle element
        new_vehicle = copy.deepcopy(vehicle)
        # Increment the 'id' attribute for the clone
        max_existing_id += 1
        new_vehicle.set('id', str(max_existing_id))
        # Update the departure time
        last_departure_time += 1  # Increase departure time by 1 second for each copy
        new_vehicle.set('depart', str(last_departure_time))
        # Append the cloned element to the list
        duplicated_vehicles.append(new_vehicle)

print(len(duplicated_vehicles))

# Append the duplicated vehicle elements to the root
for vehicle in duplicated_vehicles:
    root.append(vehicle)

# Save the modified XML to a new file
output_file = r'D:\\ASTGCN-master\\data\\gunes_kcetas\\gunes_kcetas\\gunes_kcetas_morning_30times.rou.xml'
tree.write(output_file)

print(f"Modified XML saved to '{output_file}'")
