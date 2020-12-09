import matplotlib.pyplot as plt
import numpy as np
import csv

x = []
y = []

with open('CEL_HistoricalGrantInformation 2014-7Oct2020.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if not (row[2]=='Focus area of request'):
            exists = False
            itemNum = -1
            for a in range(0,len(x)):
                if int(row[3])/int(row[4])*100 == x[a]:
                    exists = True;
                    itemNum = a;
            if exists:
                y[itemNum] = y[itemNum] + 1
            else:
                x.append(int(row[3])/int(row[4])*100)
                y.append(1)

plt.bar(x,y)
plt.show()
