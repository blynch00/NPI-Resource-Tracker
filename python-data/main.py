from config import FILE_NAME, DEFAULT_HEADERS, NEW_HEADERS, DEFAULT_DATA_PATH
from extract import return_npi_csv
from transform import transform_npi_data
from load import load_npi_data
import os
import pathlib
from pandas.io.parsers.readers import TextFileReader
# Used for argv parameters in terminal; give a path and a new name.
import sys


def etl_helper(file_path:str=DEFAULT_DATA_PATH, new_data:str=FILE_NAME) -> None:
    '''
    

    '''

    # use os.path.exists to check if directory path is valid, before checking file
    if os.path.exists(file_path) is False:
        raise ValueError(f"Error: The file {file_path} does not exist.")
    # If base data path is not default, check to see if file exists
    if file_path != DEFAULT_DATA_PATH:
        # Get the end of the path as a lowern string, then compare
        path_end = pathlib.Path(file_path).suffix.lower()
        # If incorrect file type, raise error
        if path_end != "csv":
            raise ValueError(f"Error: Incorrect File Type Given: {path_end}")

    # Check if new_data path exists, and delete it if so.
    if os.path.exists(new_data) is True:
        print("The output file already exists, and will be renamed.")
        os.rename(new_data,"previous_data.csv")
    

    # Call extract to retrieve FileIterator
    data = return_npi_csv(file_path)

    total_written  = 0

    for index, chunk in enumerate(data):
        chunk = transform_npi_data(chunk)
        total_written += load_npi_data(chunk, index)
    print(f"Finished. {total_written} lines written.")

    return None

def main(arguments:list=sys.argv) -> None:

    if len(arguments) < 3:
        print(f"Not enough parameters given. Will be defaulting to {DEFAULT_DATA_PATH} > {FILE_NAME}")
        etl_helper()
    else:
        etl_helper(arguments[1], arguments[2])

if __name__ == '__main__':
    main()