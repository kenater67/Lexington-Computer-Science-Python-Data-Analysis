import csv
from collections import Counter
import matplotlib.pyplot as plt

applicants = []

with open("data.csv", "r") as file:
    plots = csv.reader(file, delimiter=",")
    for row in plots:
        applicants.append(row[1][:4])

print(dict(Counter(applicants)))
plt.hist(applicants)
plt.show()
