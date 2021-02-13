import numpy as np
import matplotlib.pyplot as plt
import csv

category = ["Ecological Well-being", "Health & Human Services", "Arts & Culture", "Community Building", "Environment"]
arr = np.empty((0, 6), str)
moneyGranted = [[0]*5 for _ in range(6)]
moneyRequested = [[0]*5 for _ in range(6)]
perFull = [[0]*5 for _ in range(6)]


def task5(arr):  # function definition; be sure to add your task number after 'task'
    # Write your code here

    for row in arr:
        moneyGranted[int(row[1])-2015][int(row[3])-1] += int(row[4])
        moneyRequested[int(row[1])-2015][int(row[3])-1] += int(row[5]) 
    
    for i in range(6):
        for j in range(5):
            if moneyRequested[i][j] == 0:
                print(i+2015,",",category[j],":", "0.0%")
            else:
                perFull[i][j] = round((moneyGranted[i][j] / moneyRequested[i][j])*100, 2)
                print(i+2015,",",category[j],":", perFull[i][j],"%")
    for i in range(6):
        graphTitle = "Percentage fulfilled for each category in " + str(i+2015) 
        plt.title(graphTitle) 
        plt.bar(category, perFull[i])   
        plt.show()  

    

with open('CEL_HistoricalGrantInformation_2014-7Oct2020_CSV.csv', newline='') as csvfile:  # reading the csv file
    reader = csv.DictReader(csvfile)
    for row in reader:
        arr = np.append(arr, np.array([[row['organization_id'], int(row['year_id']), row['process_id'],
                                       int(row['area_id']), int(row['awarded_id']), int(row['requested_id'])]]), axis=0)

    #print(arr)

task5(arr)
