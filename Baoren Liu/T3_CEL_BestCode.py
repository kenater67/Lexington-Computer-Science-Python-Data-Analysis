import numpy as np
import matplotlib.pyplot as plt
import csv

arr = np.empty((0, 6), str)  # This is the numpy array that will be used for the entire compiled program.
#                            # It has 6 columns for organization, year, process, area, awarded, and requested.

record = np.array([0, 0, 0, 0, 0])  # create 5 values because there are 5 categories
categories = ["Ecological Well-being", "Environment", "Health & human services", "Community building", "Arts & culture"]


def task3(arr):
    for org in arr:  # adding values
        record[int(org[3])-1] += int(org[4])

    for x in range(5):  # print
        print(f"{categories[x]}: ${record[x]}")

    plt.bar(categories, record)
    plt.title("Total money given each field")
    for i in range(5):
        plt.annotate(record[i], xy=(i, record[i]), ha='center', va='bottom')
    plt.show()


with open('CEL_HistoricalGrantInformation_2014-7Oct2020_CSV.csv', newline='') as csvfile:  # reading the csv file
    reader = csv.DictReader(csvfile)
    for row in reader:
        arr = np.append(arr, np.array([[row['organization_id'], int(row['year_id']), row['process_id'], int(row['area_id']), int(row['awarded_id']), int(row['requested_id'])]]), axis=0)

    task3(arr)
