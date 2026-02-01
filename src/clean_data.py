import sys
sys.path.append(r'C:\Users\user1\OneDrive\Documents\University of Southern Calfornia\Spring 24\DSCI 510\project\clean_data_folder')

from clean_data_folder import clean_housing_data,clean_eco_data,clean_demo_data

df_housing = clean_housing_data.cleaning()
df_housing.to_csv(r'C:\Users\user1\OneDrive\Documents\University of Southern Calfornia\Spring 24\DSCI 510\project\data\processed\housing_data.csv',index=False)

df_economic = clean_eco_data.cleaning()
df_economic.to_csv(r'C:\Users\user1\OneDrive\Documents\University of Southern Calfornia\Spring 24\DSCI 510\project\data\processed\economic_data.csv',index=False)

df_demographic = clean_demo_data.cleaning()
df_demographic.to_csv(r'C:\Users\user1\OneDrive\Documents\University of Southern Calfornia\Spring 24\DSCI 510\project\data\processed\demographic_data.csv',index=False)
