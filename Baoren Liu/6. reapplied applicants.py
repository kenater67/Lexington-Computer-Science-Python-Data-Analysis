import csv

applicants = set([])
reapplied = set([])
with open("data.csv", "r") as file:
    plots = csv.reader(file, delimiter=",")
    for row in plots:
        if row[0] not in applicants:
            applicants.add(row[0])
        else:
            reapplied.add(row[0])

print(len(reapplied))
