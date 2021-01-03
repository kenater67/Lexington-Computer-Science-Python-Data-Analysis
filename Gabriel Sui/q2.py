import csv

# 2). What is the difference in amount received throughout each year for each category
# We use a 2D array to keep track of the year and category

with open('C:/Users/suiga/Downloads/data.csv') as file:
    data = csv.reader(file)
    d = ["Environment", "Health & human services", "Community building", "Arts & culture"]
    g = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for row in data:
        g[int(row[1])-2015][int(row[3])] += int(row[4])
    for y in range(4):
        print("2015 " + d[y] + ": " + str(g[0][y]))
    for x in range(5):
        for y in range(4):
            print(str(x+2016) + " " + d[y] + ": " + str(g[x+1][y]) + ", " + str(abs(g[x+1][y]-g[x][y])) + (" more than " if g[x+1][y]>g[x][y] else " less than ") + str(x+2015))
