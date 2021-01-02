import csv

yr2015 = 0
yr2016 = 0
yr2017 = 0
yr2018 = 0
yr2019 = 0
yr2020 = 0

with open('C:\\CEL\\CELdata.csv', "r") as csvfile:
    plots = csv.reader(csvfile, delimiter=",")
    for row in plots:
        if row[1] == "2015":
            yr2015 += int(row[3])

        if row[1] == "2016":
            yr2016 += int(row[3])

        if row[1] == "2017":
            yr2017 += int(row[3])

        if row[1] == "2018":
            yr2018 += int(row[3])

        if row[1] == "2019":
            yr2019 += int(row[3])

        if row[1] == "2020":
            yr2020 += int(row[3])

txt2015 = "The amount of money given away in 2015 was: ${}"
print(txt2015.format(yr2015))
txt2016 = "The amount of money given away in 2016 was: ${}"
print(txt2016.format(yr2016))
txt2017 = "The amount of money given away in 2017 was: ${}"
print(txt2017.format(yr2017))
txt2018 = "The amount of money given away in 2018 was: ${}"
print(txt2018.format(yr2018))
txt2019 = "The amount of money given away in 2019 was: ${}"
print(txt2019.format(yr2019))
txt2020 = "The amount of money given away in 2020 was: ${}"
print(txt2020.format(yr2020))