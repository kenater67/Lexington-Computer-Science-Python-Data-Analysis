import csv
import matplotlib.pyplot as plt

year2015 = 0
year2016 = 0
year2017 = 0
year2018 = 0
year2019 = 0
year2020 = 0

with open("data.csv", "r") as file:
    plots = csv.reader(file, delimiter=",")
    for row in plots:
        if row[1][:4] == "2015":
            year2015 += int(row[3])

        if row[1][:4] == "2016":
            year2016 += int(row[3])

        if row[1][:4] == "2017":
            year2017 += int(row[3])

        if row[1][:4] == "2018":
            year2018 += int(row[3])

        if row[1][:4] == "2019":
            year2019 += int(row[3])

        if row[1][:4] == "2020":
            year2020 += int(row[3])

print(year2015)
print(year2016)
print(year2017)
print(year2018)
print(year2019)
print(year2020)

plt.bar(["2015", "2016", "2017", "2018", "2019", "2020"], [year2015, year2016, year2017, year2018, year2019, year2020])
plt.title("Total money given each year")
plt.show()
