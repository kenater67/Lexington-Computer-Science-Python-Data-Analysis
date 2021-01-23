import csv
with open('C:/Users/suiga/Downloads/data.csv') as file:
    data = csv.reader(file)
    fields = ["Environment", "Health & human services", "Community building", "Arts & culture"]
    moneyGranted = [[0]*4 for _ in range(6)]
    for row in data:
        moneyGranted[int(row[1])-2015][int(row[3])] += int(row[4])
    for y in range(4):
        print(f"2015 {fields[y]}: {moneyGranted[0][y]}")
    for x in range(5):
            print(f"{x+2016} {fields[y]}: {moneyGranted[x+1][y]}, {abs(moneyGranted[x+1][y]-moneyGranted[x][y])}{(' more than ' if moneyGranted[x+1][y]>=moneyGranted[x][y] else ' less than ')}{x+2015}")
            for y in range(4):
