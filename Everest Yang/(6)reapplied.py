import csv

applicants = []
reapplied = []
with open("C:\\CEL\\CELdata.csv", "r") as csvfile:
    plots = csv.reader(csvfile, delimiter=",")
    for row in plots:
        if row[0] not in applicants:
            applicants.append(row[0])

        elif row[0] in applicants:
            reapplied.append(row[0])

txt = "{} applicants reapplied"
print(txt.format(len(reapplied)))