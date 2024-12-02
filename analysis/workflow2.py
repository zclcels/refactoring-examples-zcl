from math import *  # Import all functions from the math module

# Read sample files

# Read data from the first CSV file
#with open('data1.csv') as file1:  # (original line)
with open('samples1.csv') as file1:  # Open the file named 'samples1.csv'
    lines1 = file1.readlines()  # Read all lines from the file
    data1 = []
    for line in lines1:  # Process each line
        row = []
        for n in line.split(','):  # Split each line by commas
            row.append(float(n.strip()))  # Convert each value to float and add to the row
        data1.append(row)  # Add the row to data1

# Read data from the second CSV file
#with open('data2.csv') as file1:  # (original line)
with open('samples2.csv') as file2:  # Open the file named 'samples2.csv'
    lines2 = file2.readlines()  # Read all lines from the file
    data2 = []
    for line in lines2:  # Process each line
        row = []
        for n in line.split(','):  # Split each line by commas
            row.append(float(n.strip()))  # Convert each value to float and add to the row
        data2.append(row)  # Add the row to data2

# Read weights from the CSV file
with open('weights.csv') as filew:  # Open the file named 'weights.csv'
    linew = filew.read()  # Read the entire file content
    w = []
    for n in linew.split(','):  # Split the line by commas
        w.append(float(n.strip()))  # Convert each value to float and add to the list w

# Calculate the weighted differences
results = []
for i in range(len(data1)):  # Iterate over each row in data1
    s = 0
    for j in range(len(w)):  # Iterate over each weight
        d = data1[i][j] - data2[i][j]  # Calculate the difference between corresponding elements
        s += w[j] * abs(d)  # Multiply by the weight and add to the sum
    results.append(s)  # Append the sum to results

# Calculate the d-index
# critical = 0  # Initialize the count of critical results
# for i in range(len(results)):  # Iterate over the results
#     if results[i] > 5:  # Check if the result is greater than 5
#         critical = critical + 1  # Increment the count
# if critical == 1:  # Print the criticality message
#     print("criticality: 1 result over 5")
# else:
#     print("criticality:", critical, "results over 5")

dsum = 0  # Initialize the sum of differences
for i in range(len(results)):  # Iterate over the results
    dsum += results[i]  # Add each result to the sum
print("d-index:", dsum / len(results))  # Calculate and print the d-index
