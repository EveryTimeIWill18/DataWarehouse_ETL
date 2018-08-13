import os, sys, io
import pandas as pd
import numpy as np
import sqlite3
from pprint import pprint

header_file = "/Users/williammurphy/Desktop/Column Info_csv.csv"
jan_18 = "/Users/williammurphy/Desktop/allContactsJanuary 2018.csv"

df_header = pd.read_csv(header_file, header=0, engine='c',encoding='utf-8')
jan_18 = pd.read_csv(jan_18, header=0, encoding='ISO-8859-1',
                     engine='c', nrows=10, na_values=['na', 'NA', ' ', '    '])

index_cols = np.array(df_header['LongName'])

jan_18_cols = np.array(jan_18.columns)

missing_cols = np.isin(jan_18_cols, index_cols)

names_dict = dict()

#1495
c = 0
while c < len(index_cols):
    names_dict.update({df_header.iloc[c, 0]: df_header.iloc[c, 2]})
    c += 1

# is true
#print(list(names_dict.keys())[0] in list(jan_18.columns))
#for i , _ in enumerate(list(names_dict.keys())):
#    if list(names_dict.keys())[i] in list(jan_18.columns):
jan_18.rename(columns = names_dict, inplace=True) #this will rename columns

id_num = 6000
new_id = 'c' + str(id_num)
#for c in list(jan_18.columns):
