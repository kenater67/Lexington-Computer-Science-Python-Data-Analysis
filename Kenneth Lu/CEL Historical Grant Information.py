import matplotlib.pyplot as plt
import numpy as np
import csv

# NOTE: This program has graphs and numbers of all the problems (I think)

# 1.Organization amount awarded
def one():
    global x
    global y
    x = np.append(x,int(row[3]))

# 2.Organization amount requeste
def two():
    global x
    global y
    x = np.append(x,int(row[4]))

# 3.Organization number
def three():
    global x
    global y
    exists = False
    itemNum = -1
    for a in range(0,len(x)):
        if row[2] == x[a]:
            exists = True;
            itemNum = a;
    if exists:
        y[itemNum] += 1
    else:
        x = np.append(x,row[2])
        y = np.append(y,1)

# 4.Amount of organizations that recieved money 
def four():
    global x
    global y
    exists = False
    itemNum = -1
    for a in range(0,len(x)):
        if row[2] == x[a]:
            exists = True;
            itemNum = a;
    if exists and int(row[3]) > 0:
        y[itemNum] += 1
    elif not exists and int(row[3]) > 0:
        x=np.append(x,row[2])
        y=np.append(y,1)
    elif not exists and not int(row[3]) > 0:
        x=np.append(x,row[2])
        y=np.append(y,0)

# 5.Organization percent recieved
def five():
    global x
    global y
    exists = False
    itemNum = -1
    for a in range(0,len(x)):
        if int(row[3])/int(row[4])*100 == x[a]:
            exists = True;
            itemNum = a;
    if exists:
        y[itemNum]+=1
    else:
        x=np.append(x,int(row[3])/int(row[4])*100)
        y=np.append(y,1)

# 6.Number of times applicants applied
def six():
    global x
    global y
    exists = False
    itemNum = -1
    for a in range(0,len(x)):
        if row[0] ==  x[a]:
            exists = True;
            itemNum = a;
    if exists:
        y[itemNum]+=1
    else:
        x=np.append(x,row[0])
        y=np.append(y,1)

# 7.Differences in amount recieved in categories throughout the years
def seven():
    #Note: Sections are Ecological Well-being, Health & Human Services, Arts & Culture, Community Building, Environemnt
    global x
    global y
    exists = False
    itemNum = -1
    for a in range(0,len(x)):
        if row[1][0:5] + " " + row[2] == x[a]:
            exists = True;
            itemNum = a;
    if exists:
        y[itemNum] += int(row[3])
        #print(row[3])
    else:
        x = np.append(x,row[1][0:5] + " " + row[2])
        y = np.append(y,int(row[3]))

# 8.Total money given to each field
def eight():
    global x
    global y
    exists = False
    itemNum = -1
    for a in range(0,len(x)):
        if row[2] == x[a]:
            exists = True;
            itemNum = a;
    if exists:
        y[itemNum] += int(row[3])
    else:
        x=np.append(x,row[2])
        y=np.append(y,int(row[3]))

# 9.Percentages of categories' requested each year
def nine():
    exists = False
    itemNum = -1
    global x
    global y
    global total
    for a in range(0,len(x)):
        if row[1][0:5] + " " + row[2] == x[a]:
            exists = True;
            itemNum = a;
    if exists:
        total[itemNum]+=int(row[4])
        y[itemNum]+=int(row[3])
    else:
        x = np.append(x,row[1][0:5] + " " + row[2])
        y = np.append(y, int(row[3]))
        total = np.append(total,int(row[4]))

# 10.Total money given away each year
def ten():
    global x
    global y
    exists = False
    itemNum = -1
    for a in range(0,len(x)):
        if row[1][0:5] + " " + row[2] == x[a]:
            exists = True;
            itemNum = a;
    if exists:
        y[itemNum] += int(row[3])
        #print(row[3])
    else:
        x = np.append(x,row[1][0:5] + " " + row[2])
        y = np.append(y,int(row[3]))

# 11. Amount of applicants each year
def eleven():
    global x
    global y
    exists = False
    itemNum = -1
    for a in range(0,len(x)):
        if row[1][0:5] == x[a]:
            exists = True;
            itemNum = a;
    if exists:
        y[itemNum] += 1
    else:
        x = np.append(x,row[1][0:5])
        y = np.append(y,1)
    
        
while (True):
    # 1.Organization amount awarded
    # 2.Organization amount requested
    # 3.Organization number
    # 4.Amount of organizations that recieved money
    # 5.Organization percent recieved
    # 6.Number of times applicants applied + unique applicants for CEL grants + 
    # 7.Differences in amount recieved in categories throughout the years
    # 8.Total money given to each field + printed
    # 9.Percentages of categories' requested each year
    # 10.Total money given away each year
    # 11. Amount of applicants applied each year
    # 12. Total amount of CEL applicants (nonunique)
    # Might not do below stuff
    # Basic info
    # 13. How many years worth of data (6)
    
    print("Which of the following graphs would you like to see?\n1. Organization amount awarded\n2. Organization amount requested\n3. Organization number\n4. Amount of organizations that recieved money\n5. Organization percent recieved\n6. Number of times applicants applied\n7. Differences in amount recieved in categories throughout the years\n8. Total money given to each field\n9. Percentages of categories' requested each year\n10. Total money given away each year\n11. Amount of applicants applied each year\n12. Total amount of CEL applicants (nonunique)")
    print("Also, many specific values are printed with the graphs (they show up when you close the graph)")
    graphNum = input()

    if(graphNum == "quit" or graphNum == "Quit"):
        break

    global x
    x = np.array([], dtype='f')
    global y
    y = np.array([], dtype='f')
    # for 9
    global total
    total = np.array([], dtype='f')
    # for 12
    data=[]

    # for 11
    #totalNum=0
    
    with open('CEL_HistoricalGrantInformation 2014-7Oct2020.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        if(graphNum == "12"):
            data = list(plots)
        for row in plots:
            if not(row[0] == "Organization Name"):
                if(graphNum == "1"):
                    one()
                elif(graphNum == "2"):
                    two()
                elif(graphNum == "3"):
                    three()
                elif(graphNum == "4"):
                    four()
                elif(graphNum == "5"):
                    five()
                elif(graphNum == "6"):
                    six()
                elif(graphNum == "7"):
                    seven()
                elif(graphNum == "8"):
                    eight()
                elif(graphNum == "9"):
                    nine()
                elif(graphNum == "10"):
                    ten()
                elif(graphNum == "11"):
                    eleven()
                #elif(graphNum == "12"):
                    #twelve()
                
                    
    if(int(graphNum) > -1 and int(graphNum) < 3):
        plt.hist(x)
        plt.show()
    #required for num. 9
    if(int(graphNum) == 9):
        y = np.divide(y,total)
        y *= 100
        #for a in range(0, len(y)):
        #    y[a] *= 100
    #required for num. 7
    #Note: Sections are Ecological Well-being, Health & Human Services, Arts & Culture, Community Building, Environemnt
    if(int(graphNum) == 7):
        EWB = [0,0,0,0,0,0]
        HHS = [0,0,0,0,0,0]
        AAC = [0,0,0,0,0,0]
        CoB = [0,0,0,0,0,0]
        Env = [0,0,0,0,0,0]

        N=6
        width = 0.12
        
        for a in range(0,len(x)):
            #print(x[a][6:])
            if(x[a][6:] == "Ecological Well-being"):
                EWB[int(x[a][0:5])-2015] += y[a]
            if(x[a][6:] == "Health & Human Services"):
                HHS[int(x[a][0:5])-2015] += y[a]
            if(x[a][6:] == "Arts & Culture"):
                AAC[int(x[a][0:5])-2015] += y[a]
            if(x[a][6:] == "Community Building"):
                CoB[int(x[a][0:5])-2015] += y[a]
            if(x[a][6:] == "Environment"):
                Env[int(x[a][0:5])-2015] += y[a]
        fig, ax = plt.subplots()
        ind = np.arange(N)    # the x locations for the groups

        p1 = ax.bar(ind, EWB, width, bottom=0)
        p2 = ax.bar(ind + width, HHS, width, bottom=0)
        p3 = ax.bar(ind + 2*width, AAC, width, bottom=0)
        p4 = ax.bar(ind + 3*width, CoB, width, bottom=0)
        p5 = ax.bar(ind + 4*width, Env, width, bottom=0)
        ax.set_title('Differences in amount recieved in categories throughout the years')
        ax.set_xticks(ind + width / 2)
        ax.set_xticklabels(('2015', '2016', '2017', '2018', '2019', '2020'))
        ax.legend((p1[0], p2[0], p3[0], p4[0], p5[0]), ('Ecological Well-being', 'Health & Human Services', 'Arts & Culture', 'Community Building', 'Environemnt'))
        plt.show()
        
    if(int(graphNum) > 2 and int(graphNum) < 12 and not int(graphNum) == 7):
        plt.bar(x, y)
        plt.show()
    if(int(graphNum) == 6):
        print(str(len(x)) + " unique applicants")
        reapplied = 0
        for a in y:
            if a > 1:
                reapplied += 1
        print(str(reapplied) + " applicants reapplied")
    if(int(graphNum) == 8):
        maxArea = ""
        maxMoney = 0
        for a in range(0,len(x)):
            print(str(x[a]) + ": $" + str(y[a]))
            if(y[a] > maxMoney):
                maxMoney = y[a]
                maxArea = x[a]
        print("The area that recieved the most total award from CEL is " + maxArea + ", and they recieved $" + str(maxMoney))
    if(int(graphNum) == 9):
        for a in range(0,len(x)):
            print(str(x[a]) + ": " + str(y[a]) + "%")
    if(int(graphNum) == 10):
        for a in range(0,len(x)):
            print(str(x[a]) + ": " + str(y[a]))
    if(int(graphNum) == 11):
        for a in range(0,len(x)):
            print(str(x[a]) + ": " + str(y[a]))
    if(int(graphNum) == 12):
        print(len(data)-1)
