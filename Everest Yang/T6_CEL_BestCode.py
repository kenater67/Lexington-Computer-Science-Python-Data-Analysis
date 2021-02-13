import csv
import numpy as np

arr = np.empty((0, 6), str)

applicants = set([])
reapplied = set([])

def task6(arr):
    for row in arr:
        if row[0] not in applicants:
            applicants.add(row[0])
        else:
            reapplied.add(row[0])
txt = "{} applicants reapplied"
print(txt.format(len(reapplied)))


with open('CEL_HistoricalGrantInformation_2014-7Oct2020_CSV.csv', "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        arr = np.append(arr, np.array([[row['organization_id'], int(row['year_id']), row['process_id'], int(row['area_id']), int(row['awarded_id']), int(row['requested_id'])]]), axis=0)

task6(arr)