import pandas
# Found as return object type when returning read_csv with chunk limit.
from pandas.io.parsers.readers import TextFileReader
from .config import NEW_HEADERS, NEW_FILE_NAME
import os


def return_npi_csv(file_path="npi_data.csv", new_headers=NEW_HEADERS) -> TextFileReader:
    '''
    Returns csv contents, as an iterator of type 'TextFileReader'; loading the entire file 
    into memory would crash, as the base file is 11gb in size. 
    '''
    # Check if file already exists, deleting it if so
    if os.path.exists(NEW_FILE_NAME):
        try:
            os.remove(NEW_FILE_NAME)
        # if failed, continue execution; transform.py and MySQL have validation catches.
        except Exception as e:
            raise Exception(f"Error deleting file {NEW_FILE_NAME}: {e}")
            

    # Read csv into memory, in limited chunks
    data_iterator= pandas.read_csv(
        file_path,
        sep = ',', 
        # Skip original headers, and give new headers via names
        skiprows=1,
        header = None,
        names = new_headers,
        # Cast integer values to string during intial read
        dtype = {"NPI":str, "Zip Code": str, "Phone Number": str},
        chunksize = 500000,
        usecols = [0,5,6,20,21,22,23,24,26,47]
        ) 
    return data_iterator

if __name__ == '__main__':
    print(return_npi_csv("npi_data.csv"))