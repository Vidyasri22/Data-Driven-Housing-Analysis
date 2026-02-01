import pandas as pd
import json
import warnings
warnings.filterwarnings("ignore")

def cleaning():


    counties = []
    AMI = []
    ALI = []
    ELI = []
    VLI = []
    LI = []
    MOD = []
    sum_ALI  = 0
    sum_ELI = 0
    sum_VLI  = 0
    sum_LI = 0
    sum_MOD  = 0


    filename = r'C:\Users\user1\OneDrive\Documents\University of Southern Calfornia\Spring 24\DSCI 510\project\data\raw\Demographic data\IL.json'

    with open(filename, 'r') as json_file:
        data_dict = json.load(json_file)

    for entry in data_dict['result']['records']:
        counties.append(entry['County'])
        AMI.append(entry['AMI'])
        for i in range(1,9):
            col1 = f'ALI_{i}'
            col2 = f'ELI_{i}'
            col3 = f'VLI_{i}'
            col4 = f'LI_{i}'
            col5 = f'MOD_{i}'
            sum_ALI += float(entry[col1])
            sum_ELI += float(entry[col2])
            sum_VLI += float(entry[col3])
            sum_LI += float(entry[col4])
            sum_MOD += float(entry[col5])
        ALI.append(sum_ALI/8)
        ELI.append(sum_ELI/8)
        VLI.append(sum_VLI/8)
        LI.append(sum_LI/8)
        MOD.append(sum_MOD/8)

    df = pd.DataFrame(columns = ['counties','AMI','ALI','ELI','VLI','LI','MOD'])
    df['counties'] = counties
    df['AMI'] = AMI
    df['ALI'] = ALI
    df['ELI'] = ELI
    df['VLI'] = VLI
    df['LI'] = LI
    df['MOD'] = MOD

    df2 = pd.read_excel(r'C:\Users\user1\OneDrive\Documents\University of Southern Calfornia\Spring 24\DSCI 510\project\data\raw\Demographic data\PPH.xlsx',skiprows=9,sheet_name=1,names=['county','attributes','2010','2015','2020','2025','2030'])
    filtered_data = df2[df2['attributes'] == 'PPH']
    filtered_data.loc[:,'PPH'] = filtered_data[['2010','2015','2020','2025','2030']].mean(axis=1)
    filtered_data.reset_index(drop=True,inplace=True)

    df3 = pd.read_excel(r'C:\Users\user1\OneDrive\Documents\University of Southern Calfornia\Spring 24\DSCI 510\project\data\raw\Demographic data\EL.xlsx',sheet_name=2,skiprows=2,usecols = ['County','2022-23'],nrows=58)
    df3.rename(columns={'County':'counties','2022-23':'total_enrolled'},inplace=True)

    df = pd.concat([df,filtered_data['PPH']],axis=1)
    df = pd.concat([df,df3['total_enrolled']],axis=1)
    df['PPH'] = df['PPH'].round().astype(int)

    return df


# df.to_csv('demographic_data.csv',index=False)
