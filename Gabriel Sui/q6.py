import csv

# 6). How many applicants re-applied.
# This also returns which applicants re-applied and how many times they did

with open('C:/Users/suiga/Downloads/data.csv') as file:
    data = csv.reader(file)
    s = set()
    d = {}
    for row in data:
        if row[0] in s:
            if row[0] in d:
                d[row[0]] += 1
            else:
                d[row[0]] = 2
        else:
            s.add(row[0])
    print(len(d))
    for key in d:
        print(key + " has applied " + str(d[key]) + " times")
