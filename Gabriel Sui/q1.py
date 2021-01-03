import csv

# 1). How many unique applicants have applied for CEL grants
# We add each applicant to a set and output the length of that set

with open('C:/Users/suiga/Downloads/data.csv') as file:
    data = csv.reader(file)
    s = set()
    for row in data:
        s.add(row[0])
    print(len(s))
