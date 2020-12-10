import numpy as np
import matplotlib.pyplot as plt
import csv

rows = columns = 0
arr = np.empty((0, 5), str)


def display(arr):
    display_arr = arr

    for row in display_arr:
        if row[2] == '1':
            print(row[2])
            row[2] = 'Ecological Well-being'
        elif row[2] == '2':
            row[2] = 'Health & Human Services'
        elif row[2] == '3':
            row[2] = 'Arts & Culture'
        elif row[2] == '4':
            row[2] = 'Community Building'
        elif row[2] == '5':
            row[2] = 'Environment'

    for row in display_arr:
        print()
        for value in row:
            print(value, end=', ')
    print("\n")

def size(arr):
    print("\nrows: " + str(arr.shape[0] + 1) + ", columns: " + str(arr.shape[1]))
    print()


def categories(arr):
    ecological = health = arts = community = environment = 0
    print(arr)
    for row in arr:
        if row[2] == '1':
            ecological += 1
        elif row[2] == '2':
            health += 1
        elif row[2] == '3':
            arts += 1
        elif row[2] == '4':
            community += 1
        elif row[2] == '5':
            environment += 1

    print("Amount of Proposals In:")
    print("\tEcological Well-being: "+str(ecological))
    print("\tHealth & Human Services: "+str(health))
    print("\tArts & Culture: " + str(arts))
    print("\tCommunity Building: " + str(community))
    print("\tEnvironment: " + str(environment))
    print()

def graphs(arr):
    x = arr


def sort(arr):
    x = arr


def task(arr):
    x = arr


def menu(arr):

    while True:
        print("Menu of operations:")
        print("    1. display\n    2. size\n    3. categories\n    4. graphs\n    5. sort\n    6. task")
        choice = int(input("Choose an operation: "))

        if choice == -1:
            break
        elif choice == 1:
            display(arr)
        elif choice == 2:
            size(arr)
        elif choice == 3:
            categories(arr)
        elif choice == 4:
            graphs(arr)
        elif choice == 5:
            sort(arr)
        elif choice == 6:
            task(arr)


with open('CEL_HistoricalGrantInformation_2014-7Oct2020_CSV.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        arr = np.append(arr, np.array(
            [[row['organization_id'], row['process_id'], row['area_id'], row['awarded_id'], row['requested_id']]]),
                        axis=0)
        rows += 1

menu(arr)
