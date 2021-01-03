import csv

# 8). Which area got the most total reward from CEL
# This question can be answered with the same code as number 3

with open('C:/Users/suiga/Downloads/data.csv') as file:
    data = csv.reader(file)
    d = ["Environment", "Health & human services", "Community building", "Arts & culture"] # 0, 1, 2, 3 in the table correspond to the respective field
    g = [0,0,0,0] # given
    for row in data:
        g[int(row[3])] += int(row[4])
    for x in range(4):
        print("In the field " + d[x] + ", " + str(g[x]) + " dollars were given")
