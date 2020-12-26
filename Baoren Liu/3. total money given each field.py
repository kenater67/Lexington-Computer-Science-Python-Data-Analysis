import csv

fields = {}
with open("data.csv", "r") as file:
    plots = csv.reader(file, delimiter=",")
    for row in plots:
        if row[2] not in fields:
            fields[row[2]] = int(row[3])

        if row[2] in fields:
            fields[row[2]] = fields[row[2]] + int(row[3])

for key in fields.keys():
    print(key + ": $" + str(fields[key]))
