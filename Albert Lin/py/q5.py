import csv


area={}

with open("celdata2.csv","r") as file:
	requests=csv.reader(file,delimiter=",")
	for x in requests:
		if x[2] =="Focus area of request":
			continue
		if x[2] not in area.keys():
			area[x[2]] = [int(x[3]),int(x[4])]
		else:
			area[x[2]][0]+= int(x[3])
			area[x[2]][1]+= int(x[3])

for x in area:
	print(x+" total amt: "+str(area[x][0]))
	print(x+" total asked: "+str(area[x][1]))
	print(x+": "+str(float(area[x][0])/float(area[x][1])*100)+"%")
