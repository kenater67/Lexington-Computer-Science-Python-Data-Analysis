import csv

applicants2015 = []
applicants2016 = []
applicants2017 = []
applicants2018 = []
applicants2019 = []
applicants2020 = []

with open("data.csv", "r") as file:
    plots = csv.reader(file, delimiter=",")
    for row in plots:  # add all applicants into respective tuple
        if row[0] not in applicants2015 and row[1][:4] == "2015":
            applicants2015.append(row[0])

        if row[0] not in applicants2016 and row[1][:4] == "2016":
            applicants2016.append(row[0])

        if row[0] not in applicants2017 and row[1][:4] == "2017":
            applicants2017.append(row[0])

        if row[0] not in applicants2018 and row[1][:4] == "2018":
            applicants2018.append(row[0])

        if row[0] not in applicants2019 and row[1][:4] == "2019":
            applicants2019.append(row[0])

        if row[0] not in applicants2020 and row[1][:4] == "2020":
            applicants2020.append(row[0])

# if any applicant exists in all tuples, then print
for org in applicants2015:
    if org in applicants2016 and org in applicants2017 and org in applicants2018 and org in applicants2019 and org in applicants2020:
        print(org)
