import csv 
import matplotlib.pyplot as plt
  
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

# display data
print("Unique applicants:", len(uniqueApp))
print("Number reapplied:", len(duplicates))

year = [2015, 2016, 2017, 2018, 2019, 2020]
category = ["Ecological Well-being", "Health & Human Services", "Arts & Culture", "Community Building", "Environment"]

print("\nPer year, category: money granted and percentage fulfilled")
for i in range(6):
    for j in range(5):
        if moneyRequested[i][j] == 0:
            print(i+2015,",",j,":",moneyGranted[i][j],", 0.0%")
        else:
            perFull[i][j] = round((moneyGranted[i][j] / moneyRequested[i][j])*100, 2)
            print(i+2015,",",j,":",moneyGranted[i][j],",", perFull[i][j],"%")
for i in range(6):
    graphTitle = "Percentage fulfilled for each category in " + str(i+2015) 
    plt.title(graphTitle) 
    plt.bar(category, perFull[i])   
    plt.show()    

print("\nMoney granted per year:")
moneyPerYear = [sum(value) for value in (moneyGranted)]
for i in range(6):
    print(2015+i,":",moneyPerYear[i])
plt.title("Money granted in each year")
plt.bar(year, moneyPerYear)
plt.show()
    
print("\nMoney granted per category:")
moneyPerCategory = [sum(value) for value in zip(*moneyGranted)]
for j in range(5):
    print(j,moneyPerCategory[j])
print("Category", moneyPerCategory.index(max(moneyPerCategory)), "received the most money.")   
plt.title("Money granted to each category")
plt.bar(category, moneyPerCategory)
plt.show()

print("\nApplicants per year:")
for i in range(6):
    print(2015+i,":",numApps[i])
plt.title("Number of applicants in each year")
plt.bar(year, numApps)
plt.show()
