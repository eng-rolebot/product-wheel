import pandas as pd

delete_unusualcolor(path)def delete_unusualcolor(path):
    df1 = pd.read_excel(path,
              header=205, usecols=[0,1,4,5,7,8,9,11,12])
    print('the length of df1 is', len(df1))
    print('the number of unique color', len(df1['Color'].unique()))
    print('the number of unique next color', len(df1['Next Color Code'].unique()))
    print('the unique color exists in the color',
          (set(df1['Color'].unique()) - set(df1['Next Color Code'].unique())))
    print('the unique color exists in the next color',
          list(set(df1['Next Color Code'].unique()) - set(df1['Color'].unique())))
    newdf1 = df1.set_index('Next Color Code')
    newdf1 = newdf1.drop(list(set(df1['Next Color Code'].unique()) - set(df1['Color'].unique())), axis=0)
    print('the length of newdf1 is', len(newdf1))
