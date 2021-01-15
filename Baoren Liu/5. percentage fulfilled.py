import csv
import matplotlib.pyplot as plt

categories = {}
percentage = []
labels = []
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
    print(category+": "+str(round(categories[category][0]/categories[category][1], 2)*100)+"%")
    labels.append(category)
    percentage.append(round(categories[category][0]/categories[category][1]*100, 2))

fig, pie = plt.subplots()
pie.pie(percentage, labels=labels, startangle=90, autopct='%1.1f%%')
pie.axis('equal')
plt.title("")
plt.show()
