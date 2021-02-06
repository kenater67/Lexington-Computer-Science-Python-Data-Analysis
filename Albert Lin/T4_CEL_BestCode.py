import csv
import matplotlib.pyplot as plt
import numpy as np
ysince15=[0,0,0,0,0,0]
arr=np.empty((0,6),str)

def task4(arr):
  for x in arr:
    ysince15[int(x[1][0:4])-2015]+=1
  yr=2015
  for y in ysince15:
    print(str(yr)+": "+str(y))
    yr+=1
  plt.bar([2015,2016,2017,2018,2019,2020],ysince15)
  plt.title("Amount of grants per year")
  plt.show()


with open('CEL_HistoricalGrantInformation_2014-7Oct2020_CSV.csv', "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        arr = np.append(arr, np.array([[row['organization_id'], int(row['year_id']), row['process_id'], int(row['area_id']), int(row['awarded_id']), int(row['requested_id'])]]), axis=0)

#taking in account how the file is likely going to be read and input as a function

task4(arr)



