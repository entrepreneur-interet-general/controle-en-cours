#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 10:46:40 2017

@author: seiteta
"""
import pandas as pd


data = pd.read_excel("export2.xlsx")

print(list(data.columns.values))

data_to_export = data

data_to_export = data_to_export[['INTITULE', 'ID_CHAMBRE',
                                 'DATE_ENVOI', 'DESTINATAIRE',
                                 'NOM', 'PRENOM', 'ID_COURRIER_EXTERNE']]

data_to_export['NOM_EQUIPE'] = data_to_export['PRENOM'].astype(str).str.cat(data_to_export['NOM'].astype(str), sep= " ")

A = data_to_export.groupby('ID_COURRIER_EXTERNE').agg(lambda x: x.tolist())
B = A["NOM_EQUIPE"]
B = B.apply(lambda x: ', '.join(x))

data_to_export = A.applymap(lambda x:x[0])
data_to_export["NOM_EQUIPE"] = B
 
data_to_export = data_to_export.drop(["NOM","PRENOM"], 1)

data_to_export.columns = ["report", "juridiction", "date", "recipient", "team"]
data_to_export = data_to_export.fillna("FC")

data_to_export.to_json("data.json", orient='records')
A = data_to_export.to_dict(orient='records')

import json

data = []
with open('data.json') as f:
    for line in f:
        item = json.loads(line)
        #item = [i.replace("\'", "\"") for i in item]
        data.append(item)
        
with open('data/works.data', 'w') as f:
    for item in range(len(data[0])):
        f.write("{\"index\": {\"_index\": \"controle-en-cours\", \"_type\": \"works\"}}")
        f.write("\n")
        f.write(str(json.dumps(data[0][item])))
        f.write("\n")
        
#TODO: Delete json file
        

        
        
        
        