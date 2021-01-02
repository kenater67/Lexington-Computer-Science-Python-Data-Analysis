import csv

with open('C:\\CEL\\CELdata.csv', "r") as csvfile:
    plots = csv.reader(csvfile, delimiter=",")
    thisdict = {
    }
    for row in plots:
        thisdict.update({row[0]:1})

    keys = thisdict.keys()
    length = len(keys) - 1

    txt = "The total number of unique applicants was: {}"
    print(txt.format(length))
