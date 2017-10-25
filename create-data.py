#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 10:46:40 2017

@author: seiteta
"""
import pandas as pd
import json
import os


def convert_xlsx_to_json(xlsx_source, json_destination):
    """
        Get a xslx file and convert it to json (and save it)
        
        :param xlsx_source: The path of the xlsx file
        :type xlsx_source: str
        :param json_destination: The path of the json file
        :type json_destination: str
        
        :Example:
        >>> convert_xlsx_to_json("export.xlsx", "temp.json")
        The file export.xlsx was converted to json and saved as temp.json
    """
    # Open the file
    data = pd.read_excel(xlsx_source)
    
    # Delete unused columns
    data = data.drop(['ID_TRAVAIL', 'NUMERO', 'RAISON_SOCIALE', 'ID_TYPE_DOCUMENT'], 1)
    
    # Create a new column with name and surname
    data['NOM_EQUIPE'] = data['PRENOM'].map(str) + " " + data['NOM'].map(str)
    data = data.drop(["NOM","PRENOM"], 1)
    
    # Groupby mail ID
    data = data.groupby('ID_COURRIER_EXTERNE').agg(lambda x: x.tolist())
    
    # Build team name
    team_name = data["NOM_EQUIPE"]
    team_name = team_name.apply(lambda x: ', '.join(x))
    
    # Clean the dataframe
    data = data.applymap(lambda x:x[0])
    
    # Add the team name
    data["NOM_EQUIPE"] = team_name
     
    # Change columns name
    data.columns = ["report", "date", "recipient", "juridiction", "team"]
    
    # Specify NA values
    data = data.fillna("FC")
    
    # Export to json
    data.to_json(json_destination, orient='records')
    
    print("The file " + xlsx_source + " was converted to json and saved as " + json_destination)


def convert_json_to_data(json_source, data_destination):
    """
        Get a json file and convert it to data (and save it)
        
        :param json_source: The path of the json file
        :type json_source: str
        :param data_destination: The path of the data file
        :type data_destination: str
        
        :Example:
        >>> convert_json_to_data("temp.json", "data/works.data")
        The file temp.json was converted to data and saved as data/works.data
        The file temp.json was removed
    """
    # Create an empty list
    data = []
    
    # Read the json file
    with open(json_source) as f:
        for line in f:
            item = json.loads(line)
            data.append(item)
    os.remove(json_source)
            
    # Save it as a data file
    with open(data_destination, 'w') as f:
        for item in range(len(data[0])):
            f.write("{\"index\": {\"_index\": \"controle-en-cours\", \"_type\": \"works\"}}")
            f.write("\n")
            f.write(str(json.dumps(data[0][item])))
            f.write("\n")
            
    print("The file " + json_source + " was converted to data and saved as " + data_destination)
    print("The file " + json_source + " was removed")


# Specify filenames
xlsx_source = "export.xlsx"
json_destination = "temp.json"
json_source = json_destination
data_destination = "data/works.data"

# Convert the xlsx file to json
convert_xlsx_to_json(xlsx_source, json_destination)

# Convert the json file to data
convert_json_to_data(json_source, data_destination)        