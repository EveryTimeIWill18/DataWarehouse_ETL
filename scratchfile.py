import os, sys, io, asyncio
from functools import wraps, reduce
import multiprocessing
from collections import namedtuple, OrderedDict
import numpy as np
import pandas as pd
import pandas.core.indexing
import pandas.api.extensions


p = "/Users/williammurphy/Desktop/DW"
file = ""
if os.path.exists(p):
    print("path exists")
    file = "allContactsApril 2016.csv"
    print(file)
    os.chdir(p)
    if os.path.isfile(file):
        print("file exists")
    else:
        print(False,"file does not exist")
else:
    print(False)

# --- create pandas DataFrame
df_april_16 = pd.read_csv(filepath_or_buffer=file, header=0,
                          encoding='ISO-8859-1', chunksize=1)
first = next(df_april_16)
first_next = next(df_april_16)


# NOTE: df._data - groups columns into blocks of values
print(type(first), first.info())
#data_df = list(first._data)

memory_info = str(first._data)

