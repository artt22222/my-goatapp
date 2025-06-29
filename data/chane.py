import pandas as pd 
data = pd.read_csv("./case/skin.csv")
newco= [
    "Depression", "Anorexia", "Fever", "Weight loss", "Shivering", "Sudden death", "Hair loss", "Head drop", 
    "circling", "Cannot stand", "Cough", "Dyspnea", "Nasal discharge", "Diarrhea", "Bloody stool", "Dark/green stool",
    "Halitosis", "Skin pustules", "Body lesion", "Crusty skin", "Oral lesion", "Drooling", "Red eyes", "Tearing", 
    "Eys discharge", "lameness", "Mastitis", "Lymph nodes", "jaw edema", "Joint swelling", "Limb wounds"
]

map_columns= dict(zip(data.columns[:-1],newco))
newdata = data.rename(columns=map_columns)
newdata.to_csv("data/skin.csv", index= False, encoding='utf-8-sig')