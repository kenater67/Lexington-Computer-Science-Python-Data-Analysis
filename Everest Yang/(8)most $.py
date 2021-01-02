import csv

EcologicalWellBeing = 0
HealthHumanServices = 0
ArtsCulture = 0
CommunityBuilding = 0
Enviornment = 0

with open('C:\\CEL\\CELdata.csv', "r") as csvfile:
    plots = csv.reader(csvfile, delimiter=",")
    for row in plots:
        if row[2][:3] == "Eco":
            EcologicalWellBeing += int(row[3])

        if row[2][:6] == "Health":
            HealthHumanServices += int(row[3])

        if row[2][:4] == "Arts":
            ArtsCulture += int(row[3])

        if row[2][:3] == "Com":
            CommunityBuilding += int(row[3])

        if row[2][:3] == "Env":
            Enviornment += int(row[3])

    maxVal = EcologicalWellBeing
    max = "Ecological Well-being"
    if HealthHumanServices > maxVal:
        maxVal = HealthHumanServices
        max = "Health & Human Services"
    elif ArtsCulture > maxVal:
        maxVal = ArtsCulture
        max = "Arts & Culture"
    elif CommunityBuilding > maxVal:
        maxVal = CommunityBuilding
        max = "Community Building"
    elif Enviornment > maxVal:
        maxVal = Enviornment
        max = "Enviornment"

txtTotal = "The area that got the most total reward from CEL was: {} with ${}"
print(txtTotal.format(max, maxVal))