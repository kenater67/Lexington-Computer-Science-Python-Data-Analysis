import csv

# new code that doesn't work on my csv file but works on gabriel's
with open("data.csv", "r") as file:
    data = csv.reader(file, delimiter=",")
    categories = ["Environment", "Health & human services", "Community building", "Arts & culture"]
    record = [[0]*4 for _ in range(6)]

    for row in data:
        record[int(row[1]) - 2015][int(row[3])] += int(row[4])
    for y in range(4):
        print(f"2015 {categories[y]}: {record[0][y]}")
    for x in range(5):
        for y in range(4):
            print(f"{x+2016} {categories[y]}: {record[x+1][y]}, {abs(record[x + 1][y] - record[x][y])}" + (" more than " if record[x + 1][y] > record[x][y] else " less than ") + str(x + 2015))




''' Old code that works with my csv file



year2015 = {}
year2016 = {}
year2017 = {}
year2018 = {}
year2019 = {}
year2020 = {}
with open("data.csv", "r") as file:
    plots = csv.reader(file, delimiter=",")
    for row in plots:
        if row[1][:4] == "2015":
            if row[2] not in year2015:
                year2015[row[2]] = int(row[3])
            else:
                year2015[row[2]] += int(row[3])

        if row[1][:4] == "2016":
            if row[2] not in year2016:
                year2016[row[2]] = int(row[3])
            else:
                year2016[row[2]] += int(row[3])

        if row[1][:4] == "2017":
            if row[2] not in year2017:
                year2017[row[2]] = int(row[3])
            else:
                year2017[row[2]] += int(row[3])

        if row[1][:4] == "2018":
            if row[2] not in year2018:
                year2018[row[2]] = int(row[3])
            else:
                year2018[row[2]] += int(row[3])

        if row[1][:4] == "2019":
            if row[2] not in year2019:
                year2019[row[2]] = int(row[3])
            else:
                year2019[row[2]] += int(row[3])

        if row[1][:4] == "2020":
            if row[2] not in year2020:
                year2020[row[2]] = int(row[3])
            else:
                year2020[row[2]] += int(row[3])

print("2015:")
for key in year2015.keys():
    print(f"{key}: {year2015[key]}")

print("2016:")
for key in year2016.keys():
    try:
        print(f"{key}: {year2016[key]-year2015[key]}")
    except KeyError:  # if KeyError happens, it's because the key in 2016 doesn't exist in 2015
        print(f"{key}: {year2016[key]}")

print("2017:")
for key in year2017.keys():
    try:
        print(f"{key}: {year2017[key]-year2016[key]}")
    except KeyError:
        print(f"{key}: {year2017[key]}")

print("2018:")
for key in year2018.keys():
    try:
        print(f"{key}: {year2018[key]-year2017[key]}")
    except KeyError:
        print(f"{key}: {year2018[key]}")

print("2019:")
for key in year2019.keys():
    try:
        print(f"{key}: {year2019[key]-year2018[key]}")
    except KeyError:
        print(f"{key}: {year2019[key]}")

print("2020:")
for key in year2020.keys():
    try:
        print(f"{key}: {year2020[key]-year2019[key]}")
    except KeyError:
        print(f"{key}: {year2020[key]}")
'''
