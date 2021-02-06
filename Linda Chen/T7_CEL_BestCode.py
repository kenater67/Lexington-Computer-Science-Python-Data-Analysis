import numpy as np
import matplotlib.pyplot as plt
import csv

arr = np.empty((0, 6), str)  # This is the numpy array that will be used for the entire compiled program.
#                            # It has 6 columns for organization, year, process, area, awarded, and requested.

def task7(arr):  # function definition; be sure to add your task number after 'task'
    # Write your code here
    yearInit = 2015
    
    year = np.zeros(6, int)
    for row in arr:
        year[int(row[1])-yearInit] += int(row[4])
    count = 0
    for i in year:
        print(yearInit+count,":", i)
        count += 1
    plt.title("Money granted in each year")
    plt.bar([2015, 2016, 2017, 2018, 2019, 2020], year)
    plt.show()
    

with open('CEL_HistoricalGrantInformation_2014-7Oct2020_CSV.csv', newline='') as csvfile:  # reading the csv file
    reader = csv.DictReader(csvfile)
    for row in reader:
        arr = np.append(arr, np.array([[row['organization_id'], int(row['year_id']), row['process_id'],
                                       int(row['area_id']), int(row['awarded_id']), int(row['requested_id'])]]), axis=0)
    #print(arr)

task7(arr)  # function call; be sure to add your task number after 'task'