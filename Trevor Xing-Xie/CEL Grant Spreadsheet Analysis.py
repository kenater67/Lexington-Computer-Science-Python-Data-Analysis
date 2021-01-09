import numpy as np
import matplotlib.pyplot as plt
import csv

rows = columns = 0
arr = np.empty((0, 6), str)


def display(arr):
    display_arr = arr

    for row in display_arr:
        if row[3] == '1':
            row[3] = 'Ecological Well-being'
        elif row[3] == '2':
            row[3] = 'Health & Human Services'
        elif row[3] == '3':
            row[3] = 'Arts & Culture'
        elif row[3] == '4':
            row[3] = 'Community Building'
        elif row[3] == '5':
            row[3] = 'Environment'

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
        if row[3] == '1':
            ecological += 1
        elif row[3] == '2':
            health += 1
        elif row[3] == '3':
            arts += 1
        elif row[3] == '4':
            community += 1
        elif row[3] == '5':
            environment += 1

    print("Amount of Proposals In:")
    print("\tEcological Well-being: " + str(ecological))
    print("\tHealth & Human Services: " + str(health))
    print("\tArts & Culture: " + str(arts))
    print("\tCommunity Building: " + str(community))
    print("\tEnvironment: " + str(environment))
    print()


def graphs(arr):
    x = arr


def sort(arr):
    x = arr


def tasks(arr):
    x = arr
    print("\tMenu of tasks:")
    print("\t\t1. How many unique applicants have applied for CEL grants? "
          "\n\t\t2. What were the differences in the amount received throughout the years for each of the categories/organizations?"
          "\n\t\t3. How much total money did we give away in each field?"
          "\n\t\t4. How many applicants applied each year?"
          "\n\t\t5. Percentage of each categories' requests fulfilled each year."
          "\n\t\t6. How many applicants re-applied."
          "\n\t\t7. The total amount of money given away each year."
          "\n\t\t8. Which area got the most total reward from CEL?")
    choice = int(input("\tChoose a task: "))

    if choice == 1:
        task1(arr)
    elif choice == 2:
        task2(arr)
    elif choice == 3:
        task3(arr)
    elif choice == 4:
        task4(arr)
    elif choice == 5:
        task5(arr)
    elif choice == 6:
        task6(arr)
    elif choice == 7:
        task7(arr)
    elif choice == 8:
        task8(arr)


def task1(arr):
    # CREATING ARRAY OF: [ID, Name, # of applications]
    applicants = []
    duplicate = []
    for row in arr:
        if row[0] in applicants:
            duplicate[applicants.index(row[0])] += 1
        elif row[0] not in applicants:
            applicants.append(row[0])
            duplicate.append(1)

    print("\t\tThere were " + str(len(applicants)) + " unique applicants.")

    i = 0
    applicants_arr = np.array([[i, '0', 1]])
    for applicant in applicants:
        applicants_arr = np.append(applicants_arr, np.array([[i, applicant, 1]]), axis=0)
        i += 1

    applicants_arr = np.delete(applicants_arr, 0, 0)
    num_rows = applicants_arr.shape[0] - 1

    for j in range(num_rows):
        applicants_arr[j, 2] = duplicate[j]

    # print(applicants_arr)

    # PRINTING HOW MANY TIMES ORGANIZATIONS WHICH RE-APPLIED RE-APPLIED
    print("\t\tApplicants which re-applied:")

    for row in applicants_arr:
        if int(row[2]) > 1:
            print("\t\t\t" + row[1] + ": Applied " + row[2] + " times - ", end='')
            item_indices = np.where(arr == row[1])  # returns tuples of where row[1] is found in arr.
            #                                         For our 2d array the 1st tuple is row indices, 2nd tuple is column
            array_of_coordinates = np.array(list(zip(item_indices[0], item_indices[1])))
            row_indices = array_of_coordinates[:, 0]  # numpy way: returns new array of all 1st elements in each tuple
            # print(item_indices)
            # print(array_of_coordinates)
            # print(row_indices)

            for index in row_indices:
                if int(arr[index, 4]) == 0:
                    print("Rejected, ", end='')
                elif int(arr[index, 4]) > 0:
                    print("Accepted, ", end='')
            print()

    x = np.array(applicants_arr[:, 1])  # takes array of applicants_arr second column
    y = np.array(applicants_arr[:, 2])  # takes array of applicants_arr third column
    plt.bar(x, y)
    plt.show()


def task2(arr):
    # x is an array of 6 lists for 6 years. Each list has 5 elements for each of the four fields.
    x = np.zeros((6, 5), dtype=int)
    fields = np.array(
        ["Ecological Well-being", "Health & Human Services", "Arts & Culture", "Community Building", "Environment"])

    for row in arr:
        x[int(row[1]) - 2015, int(row[3])-1] += int(row[4])
    for i in range(6):
        print(str(2015+i)+": ")
        for j in range(5):
            print(fields[j], end='')
            print(": ", end='')
            print(x[i, j])
        print()


def task3(arr):
    ecological = health = arts = community = environment = 0
    for row in arr:
        money = int(row[4])
        if row[3] == '1':
            ecological += money
        elif row[3] == '2':
            health += money
        elif row[3] == '3':
            arts += money
        elif row[3] == '4':
            community += money
        elif row[3] == '5':
            environment += money

    print("\n\tAmount of Money Awarded In:")
    print("\t\tEcological Well-being: $" + str(ecological))
    print("\t\tHealth & Human Services: $" + str(health))
    print("\t\tArts & Culture: $" + str(arts))
    print("\t\tCommunity Building: $" + str(community))
    print("\t\tEnvironment: $" + str(environment))

    x = np.array(
        ["Ecological Well-being", "Health & Human Services", "Arts & Culture", "Community Building", "Environment"])
    y = np.array([ecological, health, arts, community, environment])
    plt.bar(x, y)
    plt.show()


def task4(arr):
    fifteen = sixteen = seventeen = eighteen = nineteen = twenty = 0
    for row in arr:
        if row[1] == '2015':
            fifteen += 1
        elif row[1] == '2016':
            sixteen += 1
        elif row[1] == '2017':
            seventeen += 1
        elif row[1] == '2018':
            eighteen += 1
        elif row[1] == '2019':
            nineteen += 1
        elif row[1] == '2020':
            twenty += 1

    print("\n\tNumber of Applicants In:")
    print("\t\t2015: " + str(fifteen) + " applicants")
    print("\t\t2016: " + str(sixteen) + " applicants")
    print("\t\t2017: " + str(seventeen) + " applicants")
    print("\t\t2018: " + str(eighteen) + " applicants")
    print("\t\t2019: " + str(nineteen) + " applicants")
    print("\t\t2020: " + str(twenty) + " applicants")

    x = np.array(["2015", "2016", "2017", "2018", "2019", "2020"])
    y = np.array([fifteen, sixteen, seventeen, eighteen, nineteen, twenty])
    plt.bar(x, y)
    plt.show()


def task5_notworking(arr):
    awd = np.zeros((6, 5), int)
    rq = np.zeros((6, 5), int)
    percent = np.zeros((6, 5), int)

    # GATHERING THROUGH: every single case.  // What is the better way to do this?

    for row in arr:
        awarded = int(row[4])
        if row[1] == '2015':
            if row[3] == '1':
                awd[0, 0] += awarded
            elif row[3] == '2':
                awd[0, 1] += awarded
            elif row[3] == '3':
                awd[0, 2] += awarded
            elif row[3] == '4':
                awd[0, 3] += awarded
            elif row[3] == '5':
                awd[0, 4] += awarded
        elif row[1] == '2016':
            if row[3] == '1':
                awd[1, 0] += awarded
            elif row[3] == '2':
                awd[1, 1] += awarded
            elif row[3] == '3':
                awd[1, 2] += awarded
            elif row[3] == '4':
                awd[1, 3] += awarded
            elif row[3] == '5':
                awd[1, 4] += awarded
        elif row[1] == '2017':
            if row[3] == '1':
                awd[2, 0] += awarded
            elif row[3] == '2':
                awd[2, 1] += awarded
            elif row[3] == '3':
                awd[2, 2] += awarded
            elif row[3] == '4':
                awd[2, 3] += awarded
            elif row[3] == '5':
                awd[2, 4] += awarded
        elif row[1] == '2018':
            if row[3] == '1':
                awd[3, 0] += awarded
            elif row[3] == '2':
                awd[3, 1] += awarded
            elif row[3] == '3':
                awd[3, 2] += awarded
            elif row[3] == '4':
                awd[3, 3] += awarded
            elif row[3] == '5':
                awd[3, 4] += awarded
        elif row[1] == '2019':
            if row[3] == '1':
                awd[4, 0] += awarded
            elif row[3] == '2':
                awd[4, 1] += awarded
            elif row[3] == '3':
                awd[4, 2] += awarded
            elif row[3] == '4':
                awd[4, 3] += awarded
            elif row[3] == '5':
                awd[4, 4] += awarded
        elif row[1] == '2020':
            if row[3] == '1':
                awd[5, 0] += awarded
            elif row[3] == '2':
                awd[5, 1] += awarded
            elif row[3] == '3':
                awd[5, 2] += awarded
            elif row[3] == '4':
                awd[5, 3] += awarded
            elif row[3] == '5':
                awd[5, 4] += awarded

    for row in arr:
        requested = int(row[5])
        if row[1] == '2015':
            if row[3] == '1':
                rq[0, 0] += requested
            elif row[3] == '2':
                rq[0, 1] += requested
            elif row[3] == '3':
                rq[0, 2] += requested
            elif row[3] == '4':
                rq[0, 3] += requested
            elif row[3] == '5':
                rq[0, 4] += requested
        elif row[1] == '2016':
            if row[3] == '1':
                rq[1, 0] += requested
            elif row[3] == '2':
                rq[1, 1] += requested
            elif row[3] == '3':
                rq[1, 2] += requested
            elif row[3] == '4':
                rq[1, 3] += requested
            elif row[3] == '5':
                rq[1, 4] += requested
        elif row[1] == '2017':
            if row[3] == '1':
                rq[2, 0] += requested
            elif row[3] == '2':
                rq[2, 1] += requested
            elif row[3] == '3':
                rq[2, 2] += requested
            elif row[3] == '4':
                rq[2, 3] += requested
            elif row[3] == '5':
                rq[2, 4] += requested
        elif row[1] == '2018':
            if row[3] == '1':
                rq[3, 0] += requested
            elif row[3] == '2':
                rq[3, 1] += requested
            elif row[3] == '3':
                rq[3, 2] += requested
            elif row[3] == '4':
                rq[3, 3] += requested
            elif row[3] == '5':
                rq[3, 4] += requested
        elif row[1] == '2019':
            if row[3] == '1':
                rq[4, 0] += requested
            elif row[3] == '2':
                rq[4, 1] += requested
            elif row[3] == '3':
                rq[4, 2] += requested
            elif row[3] == '4':
                rq[4, 3] += requested
            elif row[3] == '5':
                rq[4, 4] += requested
        elif row[1] == '2020':
            if row[3] == '1':
                rq[5, 0] += requested
            elif row[3] == '2':
                rq[5, 1] += requested
            elif row[3] == '3':
                rq[5, 2] += requested
            elif row[3] == '4':
                rq[5, 3] += requested
            elif row[3] == '5':
                rq[5, 4] += requested

    # GATHERING THROUGH: for i in range(6).  // I don't think this works

    """
    for row in arr:
        for i in range(6):
            for j in range(5):
                awarded = int(row[4])
                if row[1] == '2015':
                    if row[3] == '1':
                        awd[i, j] += awarded
                elif row[1] == '2016':
                    if row[3] == '2':
                        awd[i, j] += awarded
                elif row[1] == '2017':
                    if row[3] == '3':
                        awd[i, j] += awarded
                elif row[1] == '2018':
                    if row[3] == '4':
                        awd[i, j] += awarded
                elif row[1] == '2019':
                    if row[3] == '5':
                        awd[i, j] += awarded
                elif row[1] == '2020':
                    if row[3] == '6':
                        awd[i, j] += awarded

    for row in arr:
        for i in range(6):
            for j in range(5):
                requested = int(row[5])
                if row[1] == '2015':
                    if row[3] == '1':
                        rq[i, j] += requested
                elif row[1] == '2016':
                    if row[3] == '2':
                        rq[i, j] += requested
                elif row[1] == '2017':
                    if row[3] == '3':
                        rq[i, j] += requested
                elif row[1] == '2018':
                    if row[3] == '4':
                        rq[i, j] += requested
                elif row[1] == '2019':
                    if row[3] == '5':
                        rq[i, j] += requested
                elif row[1] == '2020':
                    if row[3] == '6':
                        rq[i, j] += requested
    """
    print(rq)
    # actually answering the question
    for i in range(6):
        for j in range(5):
            percent[i, j] = awd[i, j] / rq[i, j]

    x = np.array(["2015", "2016", "2017", "2018", "2019", "2020"])
    y = np.array(percent[0], percent[1], percent[2], percent[3], percent[4], percent[5])
    plt.bar(x, y)
    plt.show()


def task5(arr):
    awarded = np.zeros((6, 5), dtype=int)
    requested = np.zeros((6, 5), dtype=int)
    fields = np.array(
        ["Ecological Well-being", "Health & Human Services", "Arts & Culture", "Community Building", "Environment"])
    percent = 0

    for row in arr:
        awarded[int(row[1]) - 2015, int(row[3]) - 1] += int(row[4])
        requested[int(row[1]) - 2015, int(row[3]) - 1] += int(row[5])
    for i in range(6):
        print(str(2015 + i) + ": ")
        for j in range(5):
            percent = awarded[i, j] / requested[i, j]
            print(fields[j], end='')
            print(": ", end='')
            print(percent)
        print()


def task6(arr):
    applicants = []
    duplicate = []
    i = 0
    for row in arr:
        if row[0] in applicants:
            duplicate[applicants.index(row[0])] += 1
        elif row[0] not in applicants:
            applicants.append(row[0])
            duplicate.append(1)
    for item in duplicate:
        if item > 1:
            i += 1

    print("\t\t" + str(i) + " applicants re-applied for CEL grants.")


def task7(arr):
    fifteen = sixteen = seventeen = eighteen = nineteen = twenty = 0
    for row in arr:
        money = int(row[4])
        if row[1] == '2015':
            fifteen += money
        elif row[1] == '2016':
            sixteen += money
        elif row[1] == '2017':
            seventeen += money
        elif row[1] == '2018':
            eighteen += money
        elif row[1] == '2019':
            nineteen += money
        elif row[1] == '2020':
            twenty += money

    print("\t\tAmount of Money Awarded In:")
    print("\t\t\t2015: $" + str(fifteen))
    print("\t\t\t2016: $" + str(sixteen))
    print("\t\t\t2017: $" + str(seventeen))
    print("\t\t\t2018: $" + str(eighteen))
    print("\t\t\t2019: $" + str(nineteen))
    print("\t\t\t2020: $" + str(twenty))

    x = np.array(["2015", "2016", "2017", "2018", "2019", "2020"])
    y = np.array([fifteen, sixteen, seventeen, eighteen, nineteen, twenty])
    plt.bar(x, y)
    plt.show()


def task8(arr):
    ecological = health = arts = community = environment = 0
    for row in arr:
        money = int(row[4])
        if row[3] == '1':
            ecological += money
        elif row[3] == '2':
            health += money
        elif row[3] == '3':
            arts += money
        elif row[3] == '4':
            community += money
        elif row[3] == '5':
            environment += money

    dictionary = {
        "Ecological Well-being": ecological,
        "Health & Human Services": health,
        "Arts & Culture": arts,
        "Community Building": community,
        "Environment": environment
    }
    lst = list(dictionary.values())
    keys = list(dictionary.keys())
    print("\t\tThe area that got the most total reward from CEL was: ", end='')
    print(keys[lst.index(max(lst))], end='')
    print(" with $"+str(max(lst))+".")


def menu(arr):
    while True:
        print("\nMenu of operations:")
        print("    1. display\n    2. size\n    3. categories\n    4. graphs\n    5. sort\n    6. tasks")
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
            tasks(arr)


with open('CEL_HistoricalGrantInformation_2014-7Oct2020_CSV.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        arr = np.append(arr, np.array(
            [[row['organization_id'], row['year_id'], row['process_id'], row['area_id'], row['awarded_id'],
              row['requested_id']]]),
                        axis=0)
        rows += 1

menu(arr)
