import csv

ysince15=[0,0,0,0,0,0]

with open("celdata2.csv","r") as file:
	requests=csv.reader(file,delimiter=",")
	for x in requests:
		ysince15[int(x[1][0:4])-2015]+=1
yr=2015
for y in ysince15:
	print(str(yr)+": "+str(y))
	yr+=1
#only works if uses file with removed first row
