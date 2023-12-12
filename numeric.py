import pandas as pd

df = pd.read_csv('data.csv')
df['Date'] = pd.to_datetime(df['Date'],format='mixed')

def remove_symbol(cols):
    for col in cols:
        df[col] = df[col].str.replace('$', '', regex=True).astype('float64')
    return df

remove_list = ['Close/Last', 'Open', 'High', 'Low']
df = remove_symbol(remove_list)

df.to_csv('data.csv')
