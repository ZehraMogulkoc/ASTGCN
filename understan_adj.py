import csv

# Specify the input CSV file name
input_file = 'D:\ASTGCN-master\data\PEMS04\conn_graph.csv'

# Create a set to store unique values
unique_values = set()

# Read the input CSV file
with open(input_file, 'r', newline='') as infile:
    reader = csv.reader(infile)
    next(reader)  # Skip the header row if it exists
    for row in reader:
        from_value = row[0]
        to_value = row[1]
        unique_values.add(from_value)
        unique_values.add(to_value)

# Get the count of unique values
unique_count = len(unique_values)

print(f"There are {unique_count} unique values in 'from' and 'to' columns together.")
for value in unique_values:
    print(value)
