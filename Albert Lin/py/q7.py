import csv

ysince15=[0,0,0,0,0,0]
tmp=0
with open("celdata2.csv","r") as file:
	requests=csv.reader(file,delimiter=",")
	for x in requests:
		if x[1][0:4]=="2015":
			ysince15[0]+=int(x[3])
		if x[1][0:4]=="2016":
			ysince15[1]+=int(x[3])
		if x[1][0:4]=="2017":
			ysince15[2]+=int(x[3])
		if x[1][0:4]=="2018":
			ysince15[3]+=int(x[3])
		if x[1][0:4]=="2019":
			ysince15[4]+=int(x[3])
		if x[1][0:4]=="2020":
			ysince15[5]+=int(x[3])
yr=2015
for y in ysince15:
	print(str(yr)+": "+str(y))
	yr+=1