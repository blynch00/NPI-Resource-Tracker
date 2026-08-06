import pandas
# Found as return object type when returning read_csv with chunk limit.
from pandas.io.parsers.readers import TextFileReader
from .config import NEW_HEADERS, NEW_FILE_NAME
import os
from sqlalchemy import types
NEW_HEADERS = [
    "npi_code", 
    "last_name", 
    "first_name", 
    "address_1", 
    "address_2",
    "city",
    "state", 
    "zip", 
    "phone", 
    "taxonomy_code"
    ]
column_select= [0, 5, 6, 20, 21, 22, 23, 24, 26, 47]

def return_npi_csv(file_path="npi_data.csv") -> TextFileReader:
    '''
    Returns csv contents, as an iterator of type 'TextFileReader'; loading the entire file 
    into memory would crash, as the base file is 11gb in size. 
    '''
    # Check if file already exists, deleting it if so; main.py should have renamed previous file if exists
    if os.path.exists(NEW_FILE_NAME):
        try:
            os.remove(NEW_FILE_NAME)
        # if failed, continue execution; transform.py and MySQL have validation catches.
        except Exception as error_msg:
            raise error_msg
    print("NOT HERE")
    # Read csv into memory, in limited chunks
    data_iterator= pandas.read_csv(file_path, skiprows=1, header = None,usecols=column_select,names=NEW_HEADERS, chunksize = 50, sep=',') #usecols = [0,5,6,20,21,22,23,24,26,47])#, 
    
        
        
    print("OR HERE")
    return data_iterator

if __name__ == '__main__':
    print(return_npi_csv("npi_data.csv"))