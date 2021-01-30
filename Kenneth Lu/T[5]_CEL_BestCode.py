import numpy as np
import matplotlib.pyplot as plt
import csv

category = ["Ecological Well-being", "Health & Human Services", "Arts & Culture", "Community Building", "Environment"]
moneyGranted = [[0]*5 for _ in range(6)]
moneyRequested = [[0]*5 for _ in range(6)]
perFull = [[0]*5 for _ in range(6)]


def task5(arr):  # function definition; be sure to add your task number after 'task'
    # Write your code here
    for i in range(6):
        for j in range(5):
            if moneyRequested[i][j] == 0:
                print(i+2015,",",j,":", "0.0%")
            else:
                perFull[i][j] = round((moneyGranted[i][j] / moneyRequested[i][j])*100, 2)
                print(i+2015,",",j,":", perFull[i][j],"%")
    for i in range(6):
        graphTitle = "Percentage fulfilled for each category in " + str(i+2015) 
        plt.title(graphTitle) 
        plt.bar(category, perFull[i])   
        plt.show() 

    

with open('CEL_HistoricalGrantInformation_2014-7Oct2020_CSV.csv', newline='') as csvfile:  # reading the csv file
    reader = csv.DictReader(csvfile)
    for row in reader:
        moneyGranted[int(row["year_id"])-2015][int(row["area_id"])-1] += int(row["awarded_id"])
        moneyRequested[int(row["year_id"])-2015][int(row["area_id"])-1] += int(row["requested_id"]) 
        #arr = np.append(arr, np.array([[row['organization_id'], int(row['year_id']), row['process_id'],
        #                               int(row['area_id']), int(row['awarded_id']), int(row['requested_id'])]]), axis=0)
    #print(arr)

task5(perFull)  # function call; be sure to add your task number after 'task'
