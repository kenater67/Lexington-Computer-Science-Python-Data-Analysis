import csv


area={}

with open("celdata2.csv","r") as file:
	requests=csv.reader(file,delimiter=",")
	for x in requests:
		if x[2] =="Focus area of request":
			continue
		if x[2] not in area.keys():
			area[x[2]] = int(x[3])
		else:
			area[x[2]]+= int(x[3])

for x in area:
	print(x+": "+str(area[x]))
#just look at the max im too lazy to get max function working
