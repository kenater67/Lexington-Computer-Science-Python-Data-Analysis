import csv

# 7). The total amount of money given away each year.
#

with open('C:/Users/suiga/Downloads/data.csv') as file:
    data = csv.reader(file)
    g = [0,0,0,0,0,0] # given
    for row in data:
        g[int(row[1])-2015] += int(row[4])
    for x in range(6):
        print("In " + str(x+2015) + ", " + str(g[x]) + " dollars were given")
