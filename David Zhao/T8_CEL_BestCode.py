import csv
import matplotlib.pyplot as plt
import numpy as np



area = {} #index:value, the index is the area and the value is the money
with open("datafile.csv", "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row[2] in area:
            area[row[2]] = area[row[2]] + int(row[3])
        else:
            area[row[2]] = int(row[3])

highest = max(area.values())

print("The area that got the most reward was")
print(list(area.keys())[list(area.values()).index(highest)])
plt.bar(area.keys(), area.values())

for i in area.keys():
    plt.annotate(str(area[i]), xy=(i, area[i]), ha='center', va='bottom')


plt.title("How much did each area get?")
plt.xlabel("Dollars")
plt.ylabel("Area")

plt.show()
