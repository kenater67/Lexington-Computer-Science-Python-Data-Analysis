import csv
import numpy as np

arr = np.empty((0, 6), str)

def task2(arr):
    fields = ["Ecological Well-being","Health & Human Services", "Arts & Culture", "Community building", "Environment"]
    moneyGranted = [[0]*5 for _ in range(6)]
    for row in arr:
        moneyGranted[int(row[1])-2015][int(row[3])-1] += int(row[4])
    for y in range(5):
        print(f"2015 {fields[y]}: {moneyGranted[0][y]}")
    for x in range(5):
        print()
        for y in range(5):
            print(f"{x+2016} {fields[y]}: {moneyGranted[x+1][y]}, {abs(moneyGranted[x+1][y]-moneyGranted[x][y])}{(' more than ' if moneyGranted[x+1][y]>=moneyGranted[x][y] else ' less than ')}{x+2015}")

with open('C:/Users/suiga/Downloads/CEL_HistoricalGrantInformation_2014-7Oct2020_CSV.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        arr = np.append(arr, np.array([[row['organization_id'], int(row['year_id']), row['process_id'],
                                       int(row['area_id']), int(row['awarded_id']), int(row['requested_id'])]]), axis=0)
    task2(arr)
