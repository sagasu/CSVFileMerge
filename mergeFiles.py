import pandas, sys
import pandas as pd


df1 = pd.read_csv("C:/Temp/0Import.csv")
for i in range(1, 16):
    df2 = pd.read_csv(f'C:/Temp/{i}Import.csv')
    df1 = df1.append(df2)

with open('C:/Temp/result.csv', 'w', encoding='utf-8') as f:
    df1.to_csv(f, index=False)