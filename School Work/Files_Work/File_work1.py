in_file = open(r"/Users/matthew/Downloads/rci_ids.txt")

line_total = 0
count = 0

for line in in_file:
    line = line.strip("\n")
    line = float(line)
    line_total += line
    count += 1

line_total = line_total / count

print (line_total)