import pandas as pd
import delete_unusualcolor as du

def test_delete_unusualcolor():
    path = '../data/OrderColorTransitionsReport 1_1_17 - 4_22_19.xlsx'
    du(path)
    df1 = pd.read_excel('../data/OrderColorTransitionsReport 1_1_17 - 4_22_19.xlsx')
    assert df1.empty == False,'you cannot put in an empty dataframe'
