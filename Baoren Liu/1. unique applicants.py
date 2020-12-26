import csv

unique = []
with open("data.csv", "r") as file:
    plots = csv.reader(file, delimiter=",")
    for row in plots:
        if row[0] not in unique:
            unique.append(row[0])

print(len(unique))
