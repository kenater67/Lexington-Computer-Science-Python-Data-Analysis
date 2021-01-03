import csv

# 5). Percentage of each categories' requests fulfilled each year. Ex Arts and Culture Funds Given  Arts and Culture Funds Requested
# We have to use a 2D array to store both the year and the category

with open('C:/Users/suiga/Downloads/data.csv') as file:
    data = csv.reader(file)
    d = ["Environment", "Health & human services", "Community building", "Arts & culture"]
    g = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    r = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for row in data:
        g[int(row[1])-2015][int(row[3])] += int(row[4])
        r[int(row[1])-2015][int(row[3])] += int(row[5])
    for x in range(6):
        for y in range(4):
            if r[x][y] == 0:
                continue
            print(str(x+2015) + " " + d[y] + ": " + str(g[x][y]/r[x][y]*100) + "%")
