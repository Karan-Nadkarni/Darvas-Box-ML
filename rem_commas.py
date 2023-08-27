import pandas as pd

df = pd.read_csv("52_Week_High.csv")
columns_to_remove_commas = [" Today's High", " Today's Low", " Last Price"]

for column in columns_to_remove_commas:
    #df['size'] = df['size'].str.replace(',', '').astype(int)
    df[column] = df[column].replace(',','',regex=True)
    #df[column] = df[column].str.replace(',', '')

df.to_csv('52_Week_High.csv', index=False) 