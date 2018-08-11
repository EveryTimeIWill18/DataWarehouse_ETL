rom ETL import ImportData
from ETL import *



class ImportCsv(ImportData):
    """Load csv files for ETL"""
    __slots__ = ['_filepath', '_files', '_dataframe']
    def __init__(self, filepath: str, file: str):
        self._filepath = filepath.__str__()
        self._files = file.__str__()
        self._dataframe = None
        self._chunk_size = 1
        try:
            if os.path.isdir(self._filepath):
                print("PATH: {} EXISTS\n".format(self._filepath))
            else:
                raise FileExistsError("Path could not be found")
        except FileExistsError as e:
            print(e)

    def load_data(self):
        """load data set into pandas DataFrame"""
        fp = self._filepath + self._files


        self._dataframe = pd.read_csv(filepath_or_buffer=fp, header=0,
                                          engine='c', encoding='ISO-8859-1',
                                          chunksize=self._chunk_size)


class ImportCSV(ImportData):
    """Import csv file data"""

    __slots__ = ["path", "files"]
    def __init__(self, path: str, files: str):
        try:
            pass
        except:
            pass
