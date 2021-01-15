import csv
import matplotlib.pyplot as plt

def labelvalue(data):
    for i in data.keys():
        plt.annotate(str(data[i]), xy=(i, data[i]), ha='center', va='bottom')

areas = {}
with open("data.csv", "r") as file:
    plots = csv.reader(file, delimiter=",")
    for row in plots:
        if row[2] in areas:
            areas[row[2]] = areas[row[2]] + int(row[3])
        else:
            areas[row[2]] = int(row[3])

maximum = max(areas.values())
print(list(areas.keys())[list(areas.values()).index(maximum)])

plt.bar(areas.keys(), areas.values())
labelvalue(areas)
plt.title("Which area got the most reward")
plt.show()
