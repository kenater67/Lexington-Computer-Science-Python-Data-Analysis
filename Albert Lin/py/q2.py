#stupid solution, fix for years later
#also fails when x[1] isn't as expected
#also for data it cannot tell between 0 or N/A, will change to -1 maybe
import csv


area={}
orgs={}

with open("celdata2.csv","r") as file:
	requests=csv.reader(file,delimiter=",")
	for x in requests:
		if x[2] =="Focus area of request":
			continue
		if x[2] not in area.keys():
			area[x[2]] = [0,0,0,0,0,0]
			yrind = int(x[1][0:4])-2015
			area[x[2]][yrind]+=int(x[3])
		else:
			yrind = int(x[1][0:4])-2015
			area[x[2]][yrind]+=int(x[3])
		if x[0] not in orgs.keys():
			orgs[x[0]] = [0,0,0,0,0,0]
			yrind = int(x[1][0:4])-2015
			orgs[x[0]][yrind]+=int(x[3])
		else: 
			yrind = int(x[1][0:4])-2015
			orgs[x[0]][yrind]+=int(x[3])


#for areas
for x in area:
	print(x+": "+str(area[x]))
#for orgs
print("Orgs:")
for x in orgs:
	count=0
	for y in orgs[x]:
		if int(y)==0:
			count+=1
	if count<5:
		print(x+": "+str(orgs[x]))
#inefficient double loop solution, maybe store the data for "how many times asked" in another variable in dict

#also what is this question asking for needs to be more specific
