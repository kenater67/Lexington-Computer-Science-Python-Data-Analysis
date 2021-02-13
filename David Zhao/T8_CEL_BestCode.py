
import csv
import matplotlib.pyplot as plt
import numpy as np

arr=np.empty((0,6),str)



#area = {} #index:value, the index is the area and the value is the money

def task8(arr):
    area = {}
    for row in arr:
        if row[2] in area:
            area[row[2]] = area[row[2]] + int(row[3])
        else:
            area[row[2]] = int(row[3])

    highest = max(area.values());


    print("The area that got the most reward was")
    print(list(area.keys())[list(area.values()).index(highest)])
    plt.bar(area.keys(), area.values())

    for i in area.keys():
        plt.annotate(str(area[i]), xy=(i, area[i]), ha='center', va='bottom')

    plt.title("How much did each area get?")
    plt.xlabel("Dollars")
    plt.ylabel("Area")

    plt.show()




with open('CEL_HistoricalGrantInformation_2014-7Oct2020_CSV.csv', newline='') as csvfile:  # reading the csv file
    reader = csv.DictReader(csvfile)
    for row in reader:
        arr = np.append(arr, np.array([[row['organization_id'], int(row['year_id']), row['process_id'], int(row['area_id']), int(row['awarded_id']), int(row['requested_id'])]]), axis=0)


task8(arr)  # function call; be sure to add your task number after 'task'
