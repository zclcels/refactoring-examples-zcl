import csv  # Import the CSV module for reading CSV files

# Function to read a CSV file and return a list of lists of floats
def read_csv(filename):
    with open(filename) as file:
        reader = csv.reader(file)  # Create a CSV reader object
        return [[float(n) for n in line] for line in reader]  # Read and convert each value to float

# Read data from sample CSV files
data1 = read_csv('data1.csv')
data2 = read_csv('data2.csv')
weights = read_csv('weights.csv')[0]  # Read weights from the first (and only) line

# Initialize an empty list to store the results
results = [
    # For each pair of corresponding rows in data1 and data2
    sum(weights[j] * abs(data1[i][j] - data2[i][j]) for j in range(len(weights)))
    for i in range(len(data1))
]

# Define the critical threshold value
CRITICAL_THRESHOLD = 5

# Count the number of results that exceed the critical threshold
critical_count = sum(1 for result in results if result > CRITICAL_THRESHOLD)

# Print the number of critical results
if critical_count == 1:
    print("criticality: 1 result above", CRITICAL_THRESHOLD)
else:
    print(f"criticality: {critical_count} results above {CRITICAL_THRESHOLD}")
