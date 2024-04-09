import csv

with open('/Users/matthew/Documents/Python/Csv project/F1_22.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row


    column_data = [0]
    for line in csv_reader:
        line = line[0].split("\t")

        column_data.append(float(line[12]))  # Assuming the column of interest is the first one
        print(float(line[12]))  # Assuming the column of interest is the first one

average = sum(column_data) / len(column_data)

print(f"The average of the column is: {average}")