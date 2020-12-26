import csv


app=[]
reapp=[]

with open("celdata2.csv","r") as file:
	requests=csv.reader(file,delimiter=",")
	for x in requests:
		if x[0] not in app:
			app.append(x[0])
		if x[0] in app:
			reapp.append(x[0])
for y in reapp:
	print(y)