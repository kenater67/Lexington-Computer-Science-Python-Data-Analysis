import csv


app=[]

with open("celdata2.csv","r") as file:
	requests=csv.reader(file,delimiter=",")
	for x in requests:
		if x[0] not in app:
			app.append(x[0])
print("total amt of applicants: "+str(len(app)))