import csv

with open('C:/Users/suiga/Downloads/CEL_HistoricalGrantInformation_2014-7Oct2020_CSV.csv') as csvfile:
    reader = csv.reader(csvfile)
    fields = ["Ecological Well-being","Health & Human Services", "Arts & Culture", "Community building", "Environment"]
    moneyGranted = [[0]*5 for _ in range(6)]
    next(reader)
    for row in reader:
        moneyGranted[int(row[1])-2015][int(row[3])-1] += int(row[4])
    for y in range(5):
        print(f"2015 {fields[y]}: {moneyGranted[0][y]}")
    for x in range(5):
        print()
        for y in range(5):
            print(f"{x+2016} {fields[y]}: {moneyGranted[x+1][y]}, {abs(moneyGranted[x+1][y]-moneyGranted[x][y])}{(' more than ' if moneyGranted[x+1][y]>=moneyGranted[x][y] else ' less than ')}{x+2015}")
