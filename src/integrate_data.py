import pandas as pd

df1 = pd.read_csv(r'C:\Users\user1\OneDrive\Documents\University of Southern Calfornia\Spring 24\DSCI 510\project\data\processed\housing_data.csv')
df2 = pd.read_csv(r'C:\Users\user1\OneDrive\Documents\University of Southern Calfornia\Spring 24\DSCI 510\project\data\processed\demographic_data.csv')
df3 = pd.read_csv(r'C:\Users\user1\OneDrive\Documents\University of Southern Calfornia\Spring 24\DSCI 510\project\data\processed\economic_data.csv')

final_df = pd.merge(df1, df2, on='counties', how='inner')
final_df = pd.merge(final_df, df3, on='counties', how='inner')

final_df.to_csv(r'C:\Users\user1\OneDrive\Documents\University of Southern Calfornia\Spring 24\DSCI 510\project\data\processed\final_merged_data.csv',index=False)
