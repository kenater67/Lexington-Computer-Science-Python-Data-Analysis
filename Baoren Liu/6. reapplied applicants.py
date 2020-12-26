import csv

applicants = []
reapplied = []
with open("data.csv", "r") as file:
    plots = csv.reader(file, delimiter=",")
    for row in plots:
        if row[0] not in applicants:
            applicants.append(row[0])

        elif row[0] in applicants:
            reapplied.append(row[0])

print(len(reapplied))
