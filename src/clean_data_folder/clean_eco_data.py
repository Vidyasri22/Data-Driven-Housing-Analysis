import re
import pandas as pd
import json

def get_eco(filename,counties=None):
    with open(filename, 'r') as json_file:
        data_dict = json.load(json_file)

    req_dict =  data_dict['BEAAPI']['Results']['Data']

    req_list = []
    if counties:
        for entry in req_dict[1:]:
            req_list.append(entry['GeoName'])
    if counties is None:
        for i, entry in enumerate(req_dict[1:]):
            if isinstance(entry, dict):
                req_list.append(entry['DataValue'])
    return req_list

def cleaning():

    df_economic = pd.DataFrame(columns=['counties','GDP','PI','POP','PCI'])
    df_economic['counties'] = get_eco(r"C:\Users\user1\OneDrive\Documents\University of Southern Calfornia\Spring 24\DSCI 510\project\data\raw\Economic data\GDP.json",counties=True)
    df_economic['GDP'] = get_eco(r"C:\Users\user1\OneDrive\Documents\University of Southern Calfornia\Spring 24\DSCI 510\project\data\raw\Economic data\GDP.json")
    df_economic['PI'] = get_eco(r"C:\Users\user1\OneDrive\Documents\University of Southern Calfornia\Spring 24\DSCI 510\project\data\raw\Economic data\PI.json")
    df_economic['POP'] = get_eco(r"C:\Users\user1\OneDrive\Documents\University of Southern Calfornia\Spring 24\DSCI 510\project\data\raw\Economic data\POP.json")
    df_economic['PCI'] = get_eco(r"C:\Users\user1\OneDrive\Documents\University of Southern Calfornia\Spring 24\DSCI 510\project\data\raw\Economic data\PCI.json")

    excel_cols = ['LAUS CODE','STATE CODE','COUNTY CODE','COUNTY NAME','YEAR','UNNAMED','LABOUR FORCE','EMPLOYED','UNEMPLOYED','UNEMPLOYMENT RATE']
    lf_path = r'C:\Users\user1\OneDrive\Documents\University of Southern Calfornia\Spring 24\DSCI 510\project\data\raw\Economic data\labour force.xlsx'
    cols_to_add =['LABOUR FORCE','EMPLOYED','UNEMPLOYED','UNEMPLOYMENT RATE']
    df_lf = pd.read_excel(lf_path,skiprows=192,nrows=58,names=excel_cols)
    df_economic = pd.concat([df_economic, df_lf[cols_to_add]], axis=1)

    return df_economic
