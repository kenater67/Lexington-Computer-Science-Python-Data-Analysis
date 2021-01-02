import csv 
import matplotlib.pyplot as plt
import numpy as np
  
filename = "CEL_edited.csv"
  
uniqueApp = []
duplicates = []
numApps = [0] * 6
moneyGranted = [[0]*5 for _ in range(6)]
moneyRequested = [[0]*5 for _ in range(6)]
perFull = [[0]*5 for _ in range(6)]

with open(filename, 'r') as csvfile: 
    csvreader = csv.reader(csvfile) 
      
    for row in csvreader: 
        # number of unique applicants
        if row[0] not in uniqueApp:
            uniqueApp.append(row[0])
        else:
            if row[0] not in duplicates:
                duplicates.append(row[0])
        
        # money requested and granted to each year, category
        moneyGranted[int(row[1])-2015][int(row[2])-1] += int(row[3])
        moneyRequested[int(row[1])-2015][int(row[2])-1] += int(row[4])
        
        # applications per year, category
        numApps[int(row[1])-2015] += 1

print("Unique applicants:", len(uniqueApp))
print("Number reapplied:", len(duplicates))

year = [2015, 2016, 2017, 2018, 2019, 2020]
category = ["Ecological Well-being", "Health & Human Services", "Arts & Culture", "Community Building", "Environment"]

print("\nPer year, category: money granted and percentage fulfilled")
years = range(6)
categories = range(5)
for i in years:
    for j in categories:
        if moneyRequested[i][j] == 0:
            print(i+2015,",",j,":",moneyGranted[i][j],", 0.0%")
        else:
            perFull[i][j] = round((moneyGranted[i][j] / moneyRequested[i][j])*100, 2)
            print(i+2015,",",j,":",moneyGranted[i][j],",", perFull[i][j],"%")
for i in years:
    graphTitle = "Percentage fulfilled for each category in " + str(i+2015) 
    plt.title(graphTitle) 
    plt.bar(category, perFull[i])   
    plt.show()    

moneyPerYear = [0] * 6
print("\nMoney granted per year:")
for i in years:
    x = sum(moneyGranted[i])
    print(2015+i,":",x)
    moneyPerYear[i] = x
plt.title("Money granted in each year")
plt.bar(year, moneyPerYear)
plt.show()
    
moneyPerCategory = [0] * 5
print("\nMoney granted per category:")
highest = 0
maxCategory = ""
for j in categories:
    x = 0
    for i in years:
        x += moneyGranted[i][j]
    print(j,":",x)
    if x > highest:
        highest = x
        maxCategory = j
    moneyPerCategory[j] = x
print("Category", maxCategory, "received the most money.")
plt.title("Money granted to each category")
plt.bar(category, moneyPerCategory)
plt.show()

appsPerYear = [0] * 6

print("\nApplicants per year:")
for i in years:
    total = 0
    total += numApps[i]
    print(2015+i,":",total)
    appsPerYear[i] = total
plt.title("Number of applicants in each year")
plt.bar(year, numApps)
plt.show()