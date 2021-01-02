import csv
import matplotlib.pyplot as plt

difference = {}
with open("data.csv", "r") as file:
    plots = csv.reader(file, delimiter=",")
    for row in plots:
        if row[2] not in difference.keys():
            difference[row[2]] = int(row[4])-int(row[3])

        else:
            difference[row[2]] = difference[row[2]]+int(row[4])-int(row[3])

print(difference)
plt.bar(difference.keys(), difference.values())
plt.title("How much money did each area not get")
plt.show()
