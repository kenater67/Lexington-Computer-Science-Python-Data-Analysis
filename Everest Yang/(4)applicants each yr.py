import csv

with open('C:\\CEL\\CELdata.csv', "r") as csvfile:
    plots = csv.reader(csvfile, delimiter=",")
    dict2015 = {

    }
    dict2016 = {

    }
    dict2017 = {

    }
    dict2018 = {

    }
    dict2019 = {

    }
    dict2020 = {

    }
    for row in plots:
        if row[1] == "2015":
            dict2015.update({row[0]:1})
        if row[1] == "2016":
            dict2016.update({row[0]:1})
        if row[1] == "2017":
            dict2017.update({row[0]:1})
        if row[1] == "2018":
            dict2018.update({row[0]:1})
        if row[1] == "2019":
            dict2019.update({row[0]:1})
        if row[1] == "2020":
            dict2020.update({row[0]:1})


    keys2015 = dict2015.keys()
    keys2016 = dict2016.keys()
    keys2017 = dict2017.keys()
    keys2018 = dict2018.keys()
    keys2019 = dict2019.keys()
    keys2020 = dict2020.keys()

    txt2015 = "The total number of unique applicants in 2015 was: {}"
    print(txt2015.format(len(keys2015)))
    txt2016 = "The total number of unique applicants in 2016 was: {}"
    print(txt2016.format(len(keys2016)))
    txt2017 = "The total number of unique applicants in 2017 was: {}"
    print(txt2017.format(len(keys2017)))
    txt2018 = "The total number of unique applicants in 2018 was: {}"
    print(txt2018.format(len(keys2018)))
    txt2019 = "The total number of unique applicants in 2019 was: {}"
    print(txt2019.format(len(keys2019)))
    txt2020 = "The total number of unique applicants in 2020s was: {}"
    print(txt2020.format(len(keys2020)))
