import os
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from itertools import chain
from pprint import pprint

header_file = "O:\\Information Technology\\Data Services\\Data Warehouse QA\\NYCWell_raw_monthly\\Column Info_csv.csv"
june_2018 = "O:\\Information Technology\\Data Services\\Data Warehouse QA\\NYCWell_raw_monthly\\allContactsJune 2018.csv"

# read in the header file as a data frame
df_header = pd.read_csv(header_file, header=0, engine='c',
                        encoding='utf-8')
index_cols = np.array(df_header['LongName'])

# make a data frame for april 2016 data
june_18 = pd.read_csv(june_2018, header=0, engine='c',
                       encoding='ISO-8859-1', chunksize=1000,
                       na_values=['na', 'NA', ' ', '    '],
                      low_memory=False)

current_chunk = next(june_18)
names_dict = dict()
cntr = 0
while cntr < len(index_cols):
    names_dict.update({df_header.iloc[cntr, 0]: df_header.iloc[cntr, 2]})
    cntr += 1

# rename the columns that have matching names
current_chunk.rename(columns = names_dict, inplace=True)
#pprint(list(current_chunk.columns))


# for ids that do not have a c-id, assign them a c-id
id_num = 6000
new_id = 'c' + str(id_num)
for c in list(current_chunk.columns):
        if len(c) >= 8:
            new_id = 'c' + str(id_num)
            current_chunk.rename(columns = {c: new_id}, inplace=True)
            id_num += 1

# maintain a list of null values
nulls_dict = dict()
# update nulls_dict to calculate all null values
for i, _ in enumerate(list(current_chunk.columns)):
    k = '{}'.format(list(current_chunk.columns)[i])
    col = current_chunk[k]
    if k not in list(nulls_dict.keys()):
       na_value = col.isnull().sum()
       nulls_dict.update({str(k): na_value})
    else:
        na_value = col.isnull().sum()
        nulls_dict[k] = na_value

pprint(nulls_dict)

# check that all columns have been renamed
#pprint(list(current_chunk.columns))

#pprint(len(list(current_chunk.columns)))
#pprint(current_chunk.head(10))
#pprint(current_chunk.info())
#pprint(current_chunk['{}'.format(list(current_chunk.columns))].dtypes)

#types = [t for t in list(current_chunk.dtypes)]
