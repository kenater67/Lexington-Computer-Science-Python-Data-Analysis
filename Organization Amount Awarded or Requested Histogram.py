import matplotlib.pyplot as plt
import numpy as np
import csv

x = []

print("Would you like the histogram of the Amount Awarded or the Amount Requested?")
ans = input()

with open('CEL_HistoricalGrantInformation 2014-7Oct2020.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        # row[3] shows recieved amount, "Amount Awarded"
        # row[4] shows requested amount "Amount requested"
        if not(row[4] == "Amount requested"):
            if ans == "Amount Awarded" or ans == "Amount awarded" or ans == "amount awarded":
                x.append(int(row[3]))
            elif ans == "Amount Requested" or ans == "Amount requested" or ans == "amount requested":
                x.append(int(row[4]))
            else:
                print("Answer could not be understood, please run the program again")

plt.hist(x)
plt.show()
