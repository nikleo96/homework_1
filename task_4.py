import json
import pickle
import csv

label_list = ["Model", "Year", "Horsepower", "Engine size"]
information_dict = {"car": []}

with open("text_4.csv", "r", encoding="utf-8") as f:
    file_reader = csv.reader(f, delimiter=";")
    for row in file_reader:
        d = {label_list[i]: el for i, el in enumerate(row)}
        information_dict["car"].append(d)

with open("text_4.json", "w") as f:
    json.dump(information_dict, f)

with open('text_4.pickle', 'wb') as f:
    pickle.dump(information_dict, f) 


