import csv

categories = {}
with open("data.csv", "r") as file:
    plots = csv.reader(file, delimiter=",")
    for row in plots:
        awarded = int(row[3])
        requested = int(row[4])
        if row[2] not in categories.keys():
            categories[row[2]] = [awarded, requested]

        else:
            categories[row[2]] = [categories[row[2]][0]+awarded, categories[row[2]][1]+requested]

for category in categories.keys():
    print(category+": "+str(round(categories[category][0]/categories[category][1], 2))+"%")
