# ALL src files grouped as a module, to reduce total imports and name obsfucation
from src import return_npi_csv, transform_npi_data, load_npi_data, NEW_FILE_NAME, DEFAULT_DATA_PATH

# Used for file pathing, file handling, and command line arguments.
import sys
import os
import pathlib

def etl_helper(file_path:str=DEFAULT_DATA_PATH, new_data:str=NEW_FILE_NAME) -> None:
    '''
    etl_helper is called via main() to run the ETL pipeline. It first checks
    if the given csv path is valid, and if it is a .csv; additionally, this checks the 
    output file name, renaming to clear name for pipeline.
    '''

    # use os.path.exists to check if directory path is valid, before checking file
    if os.path.exists(file_path) is False:
        print(f"Error: The file {file_path} does not exist. Will default to {DEFAULT_DATA_PATH}")
        file_path = DEFAULT_DATA_PATH
    # If base data path is not default, check to see if file exists
    if file_path != DEFAULT_DATA_PATH:
        # Get the end of the path as a lower string, then compare
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
    print("============= Beginning ETL Process for File =============")
    total_written  = 0

    for index, chunk in enumerate(data):
        chunk = transform_npi_data(chunk)
        total_written += load_npi_data(chunk, index, new_data)
    print(f"=============  {total_written} lines written to file. =============")

    return None


def main(arguments:list=sys.argv) -> None:
    '''
    main function; calls etl_helper after checking command arguments.
    '''
    if len(arguments) < 3:
        print(f"Not enough parameters given. Will be defaulting to {DEFAULT_DATA_PATH} > {NEW_FILE_NAME}")
        etl_helper()
    else:
        etl_helper(arguments[1], arguments[2])

if __name__ == '__main__':
    main()