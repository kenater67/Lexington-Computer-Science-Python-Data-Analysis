import csv
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def labelvalue(data):
    for i in data.keys():
        plt.annotate(str(data[i]), xy=(i, data[i]), ha='center', va='bottom')

applicants = np.array([])
with open("data.csv", "r") as file:
    plots = csv.reader(file, delimiter=",")
    for row in plots:
        applicants = np.append(applicants, row[1][:4])

result = dict(Counter(applicants))
print(result)
plt.bar(result.keys(), result.values())
plt.title("How many applicants applied each year?")
labelvalue(result)
plt.show()
