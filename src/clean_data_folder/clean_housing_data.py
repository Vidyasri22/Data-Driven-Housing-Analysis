import re
import pandas as pd
import json

def fetch_values(df,counties=None):
    series = df.squeeze()
    series = series[2:]
    list_county = series.index.tolist()
    if counties:
        words = []
        for text in list_county:
            index_county = text.find("County")
            word = text[:index_county].strip()
            words.append(word)
        return words
    if counties is None:
        estimates = series[::].tolist()
        return estimates

def cleaning():

    df1 = pd.read_csv(r'C:\Users\user1\OneDrive\Documents\University of Southern Calfornia\Spring 24\DSCI 510\project\data\raw\Housing data\max_price.csv')
    counties = fetch_values(df1,counties=True)
    high_estimates = fetch_values(df1)

    df2 = pd.read_csv(r'C:\Users\user1\OneDrive\Documents\University of Southern Calfornia\Spring 24\DSCI 510\project\data\raw\Housing data\median_price.csv')
    mid_estimates = fetch_values(df2)

    df3 = pd.read_csv(r'C:\Users\user1\OneDrive\Documents\University of Southern Calfornia\Spring 24\DSCI 510\project\data\raw\Housing data\min_price.csv')
    low_estimates = fetch_values(df3)

    df_housing = pd.DataFrame(columns=['counties','High','Median','Low'])
    df_housing['counties'] = counties
    df_housing['High'] = high_estimates
    df_housing['Median'] = mid_estimates
    df_housing['Low'] = low_estimates
    df_housing = df_housing.applymap(lambda x:x.replace(',','') if isinstance(x,str) else x)
    for column in df_housing.columns[1:]:
        df_housing[column] = df_housing[column].astype(float)

    return df_housing
