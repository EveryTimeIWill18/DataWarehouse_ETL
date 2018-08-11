from ETL_one import *
from ETL_one import (memory_footprint, file_search,
                     file_to_read_in)




def main():
    fp = "D:\\RawCSVs"
    data = file_search(dir_=fp)
    num_rows = 0
    samples = list()
    number_samples = 0

    print("memory usage: {}".format(memory_footprint()))
    print("=======================")
    start = time.time()
    for d in data:
        num_rows += 100
        while number_samples < 1:
            print("Sample DataFrame Statistics")
            print("=======================")
            str(d.info())
            number_samples += 1
    end = time.time()
    print("number of rows read: {}".format(num_rows))
    print("file number: {}".format(ITERATOR))
    print("memory usage: {}".format(memory_footprint()))
    print("run time: {}".format((end-start)))
    print("=======================")


if __name__ == '__main__':
    main()
