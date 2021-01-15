import csv

unique = set([])
with open("data.csv", "r") as file:
    plots = csv.reader(file, delimiter=",")
    for row in plots:
        if row[0] not in unique:
            unique.add(row[0])

print(len(unique))
