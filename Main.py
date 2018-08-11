from ETL_two import *
from ETL_two import ImportCsv

def main():
    """Main function"""
    f_path = "/Users/williammurphy/Desktop/DW"
    file = "/allContactsApril 2016.csv"

    load_one = ImportCsv(filepath=f_path, file=file)
    load_one.chunk_size = 1
    load_one.load_data()
    print(next(load_one._dataframe))




if __name__ == '__main__':
    main()

