import csv

# 4). How many applicants applied each year
#

with open('C:/Users/suiga/Downloads/data.csv') as file:
    data = csv.reader(file)
    a = [0,0,0,0,0,0]
    for row in data:
        a[int(row[1])-2015] += 1
    for x in range(6):
        print("In " + str(x+2015) + ", " + str(a[x]) + " applicants applied")
