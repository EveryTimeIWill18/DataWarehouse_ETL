import os, io, sys
import re
from pprint import pprint
import time
import psutil
import requests
from functools import reduce, wraps
from itertools import chain
import numpy as np
import pandas as pd
from numba import cuda

# --- gloabal variables
ITERATOR = 0
en_url = "https://docs.python.org/2.4/lib/standard-encodings.html"
try:
    r = requests.get(url=en_url, allow_redirects=True)
    if r.status_code == 200:
        print("Connection successful: status[{}]".format(r.status_code))
        print("==================================\n")
        p = re.compile('valign="baseline".*')
        raw_encodings = re.findall(p, r.text)
        encodings = [str(e).lstrip('valign="baseline">').rstrip('</td>') for e in raw_encodings]
    else:
        raise ConnectionError("Failed to connect: status[{}".format(r.status_code))
except ConnectionError as e:
    print(e)

print('utf-8' in encodings)

# --- memory functions
def memory_footprint() -> float:
    """Get memory usage(MB) used by Python"""
    usage = psutil.Process(os.getpid())\
                        .memory_info()\
                        .rss
    #mem_percent = psutil.Process(os.getpid())\
    #                        .memory_percent(memtype="rss")
    return (usage/1024**2)


# --- process the data into a DataFrame
def file_to_read_in(num_files: int, encoding_: str, chunk_size: int):
    """read in file and process it"""
    def process_file(f: callable):
        @wraps(f)
        def wrapper(*args, **kwargs):
            fn = f(*args, **kwargs)
            global ITERATOR
            while ITERATOR < num_files:
                current = fn[ITERATOR]
                print("current file: {}".format(current))
                df = pd.read_csv(filepath_or_buffer=current, header=0,
                                 engine='c', encoding=str(encoding_),
                                 chunksize=int(chunk_size), low_memory=True,
                                 na_values=['', 'NULL', 'N/A', 'null'])
                for chunk in df:
                    yield chunk
                ITERATOR += 1
        return wrapper
    return process_file


# --- get directory
@file_to_read_in(1, 'ISO-8859-1', chunk_size=100)
def file_search(dir_: str) -> (list, str):
    """search for the desired folder"""
    if os.path.isdir(dir_):
        os.chdir(dir_)
        #print("Directory exists")
        all_files = list(chain.from_iterable(
            [f for _, _, f in os.walk(dir_) if len(f) > 0]
        ))
        return all_files
    else:
        return "Directory not found."
