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


txtEco = "The total amount of money given away in Ecological Well-Being was: ${}"
print(txtEco.format(EcologicalWellBeing))
txtHealth = "The total amount of money given away in the field Health & Human Services was: ${}"
print(txtHealth.format(HealthHumanServices))
txtArts= "The total amount of money given away in the field Arts & culture was: ${}"
print(txtArts.format(ArtsCulture))
txtCom = "The total amount of money given away in the field Community Building was: ${}"
print(txtCom.format(CommunityBuilding))
txtEnv = "The total amount of money given away in field Environment was: ${}"
print(txtEnv.format(Enviornment))