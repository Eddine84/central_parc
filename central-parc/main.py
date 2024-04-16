# import csv

# with open("./weather_data.csv") as data:
#    data_list =  csv.reader(data)
#    temparetures = []
#    next(data_list) 
#    for line in data_list:
#      temparetures.append(int(line[1]))
#    print(temparetures)


# data = pd.read_csv("./weather_data.csv")
# monday_temp = data[data.day == "Monday"]
# print(monday_temp.temp[0])
# #print(monday_temp.temp * 9/5 + 32)

# data = {
#     "student":["djamel","pasca","alex"],
#     "age":[39,40,29],
#     "country":["algeria", "france","switzerland"]
# }

# data_frame = pd.DataFrame(data)
# data_frame.to_csv("data.csv")
# print(data_frame[data_frame.student == "djamel"].age)


# liste_couleur_grey = liste_couleurs[liste_couleurs["Primary Fur Color"] == "Gray"].tolist()

# print(liste_couleur_grey)




# import pandas as pd
# data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# lignes_couleurs_grise = data[data["Primary Fur Color"] == "Gray"]
# colonne_couleurs_grise = lignes_couleurs_grise["Primary Fur Color"]
# first_result = len(colonne_couleurs_grise)

# lignes_couleurs_noire = data[data["Primary Fur Color"] == "Black"]
# colonne_couleurs_noire = lignes_couleurs_noire["Primary Fur Color"]
# second_result = len(colonne_couleurs_noire)

# lignes_couleurs_cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
# colonne_couleurs_cinnamon = lignes_couleurs_cinnamon["Primary Fur Color"]
# third_result = len(colonne_couleurs_cinnamon)


# data = {
#     "Fur Color":["Gray","Black","Cinnamon"],
#     "Count":[first_result,second_result,third_result]
# }

# data_frame = pd.DataFrame(data)
# data_frame.to_csv("filter_ecureuil.csv")













