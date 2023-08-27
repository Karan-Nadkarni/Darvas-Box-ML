import pandas as pd

df = pd.read_csv("52_Week_High.csv")
# Specify column_names in  which you want to remove commas in below list
columns_to_remove_commas = [" Today's High", " Today's Low", " Last Price"]

# For loop will iterate thorugh each column removing commas for every value with replace()
# In replace function , 1st parameter is what you want to replace in string, 2nd parameter is what you want to replace it with.
for column in columns_to_remove_commas:
    #df['size'] = df['size'].str.replace(',', '').astype(int)
    df[column] = df[column].replace(',','',regex=True)
    #df[column] = df[column].str.replace(',', '')

# Overwrite changes to file
df.to_csv('52_Week_High.csv', index=False) 
