import matplotlib.pyplot as plt
import numpy as np
import csv

x = []
y = []

print("Would you like the bar graph of the amount of organizations of each category or the amount that made money in each category? (1 or 2)")
answer = input()

with open('CEL_HistoricalGrantInformation 2014-7Oct2020.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if not (row[2]=='Focus area of request'):
            exists = False
            itemNum = -1
            for a in range(0,len(x)):
                if row[2] == x[a]:
                    exists = True;
                    itemNum = a;
            if answer == "1" or answer == "one" or answer == "One":
                if exists:
                     y[itemNum] += 1
                else:
                    x.append(row[2])
                    y.append(1)
            elif answer == "2" or answer == "two" or answer == "Two":
                if exists and int(row[3]) > 0:
                    y[itemNum] += 1
                elif not exists and int(row[3]) > 0:
                    x.append(row[2])
                    y.append(1)
                elif not exists and not int(row[3]) > 0:
                    x.append(row[2])
                    y.append(0)
            else:
                print("Answer was unrecognizable, please run the program again")

plt.bar(x,y)
plt.show()
