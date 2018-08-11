import os, sys, io
import abc
import re
from functools import wraps, reduce
import multiprocessing
from collections import namedtuple, OrderedDict
import numpy as np
import pandas as pd
import boto3
import botocore


class ImportData(metaclass=abc.ABCMeta):
    """interface for creating a
    data stream connection"""

    def set_data_connection(self, *args, **kwargs):
        """create a connection to a
        data source"""



