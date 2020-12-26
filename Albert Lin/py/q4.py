import csv

ysince15=[0,0,0,0,0,0]

with open("celdata2.csv","r") as file:
	requests=csv.reader(file,delimiter=",")
	for x in requests:
		if x[1][0:4]=="2015":
			ysince15[0]+=1
		if x[1][0:4]=="2016":
			ysince15[1]+=1
		if x[1][0:4]=="2017":
			ysince15[2]+=1
		if x[1][0:4]=="2018":
			ysince15[3]+=1
		if x[1][0:4]=="2019":
			ysince15[4]+=1
		if x[1][0:4]=="2020":
			ysince15[5]+=1
yr=2015
for y in ysince15:
	print(str(yr)+": "+str(y))
	yr+=1