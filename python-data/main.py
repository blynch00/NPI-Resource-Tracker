# ALL src files grouped as a module, to reduce total imports and name obsfucation
from src import return_npi_csv, transform_npi_data, load_npi_data, NEW_FILE_NAME, DEFAULT_DATA_PATH
from dotenv import load_dotenv
# Used for file pathing, file handling, and command line arguments.
import sys
import os
import pathlib
# Used to connect to DB, cast types and insert csv data
import sqlalchemy


def etl_helper(file_path:str=DEFAULT_DATA_PATH, new_data:str=NEW_FILE_NAME, engine=None, table_name:str="providers") -> None:
    '''
    etl_helper is called via main() to run the ETL pipeline. It first checks
    if the given csv path is valid, and if it is a .csv; additionally, this checks the 
    output file name, renaming to clear name for pipeline.
    '''

    # use os.path.exists to check if directory path is valid, before checking file
    if os.path.exists(file_path) is False:
        if file_path != DEFAULT_DATA_PATH and os.path.exists(DEFAULT_DATA_PATH) is True:
            print(f"Error: The file {file_path} does not exist. Will default to {DEFAULT_DATA_PATH}")
            file_path = DEFAULT_DATA_PATH
        else:
            raise ValueError(f"Error: The file {file_path} does not exist. Please check path.")
    
    # Get the end of the path as a lower string, then compare
    path_end = pathlib.Path(file_path).suffix.lower()
    # If incorrect file type, raise error
    if path_end != ".csv":
        raise ValueError(f"Error: Incorrect File Type Given: {path_end}")

    # Check if new_data path exists, and delete it if so.
    if os.path.exists(new_data) is True:
        print("The output file already exists, and will be renamed.")
        os.rename(new_data,"previous_data.csv")

    print("============= Beginning ETL Process for File =============")
    # Call extract to retrieve FileIterator
    data = return_npi_csv(file_path)
    total_written  = 0
    # index can be passed to load_npi_data to initially insert headers into CSV
    for index, chunk in enumerate(data):
        #call transform.py
        chunk = transform_npi_data(chunk)
        # Increase count by # of SQL lines written
        total_written += load_npi_data(chunk, index, new_data, engine, table_name)
        print(f"Iteration: {index}. {total_written} lines to SQL.")
    print(f"=============  {total_written} lines written to SQL. =============")


def sql_connection(login) -> sqlalchemy.Engine | None:
    '''
    Uses .env variables to attempt a connection to the SQL DB; 
    cannot check if connection is valid, just if login is none 
    '''
    if login is None:
        return None
    # Create engine does not test connection, so connection must be tested after.
    engine = sqlalchemy.create_engine(login, echo=False)
    try:
        # Execution failure will be caught, and cause only CSV to be written to.
        with engine.connect() as connection:
            connection.execute(sqlalchemy.text("SELECT 1"))
    except Exception as error_msg:
        print(f"Error: {error_msg}. Will run in CSV only mode.")
        # engine=None prevents dataframe from attempting to write to SQL.
        return None
    print("Connection to SQL DB successful.")
    return engine


def main(arguments:list=sys.argv) -> None:
    '''
    main (); Loads .env, calls sql_connection, checks argv[] arguments,
    then calls helper function to begin ETL process.
    '''
    # Load environment variables to connect to DB, get strings
    load_dotenv()
    login = os.environ['DB_PATH']
    table_name = os.environ['TABLE_NAME']

    # Create engine type from SQLAlchemy, for use in load.py
    engine = sql_connection(login)
    # Determine if CLI arguments were given, or if defaults should be used.
    file_path,new_data = DEFAULT_DATA_PATH, NEW_FILE_NAME
    if len(arguments) < 3:
        # Will change to requiring valid argv[] inputs.
        print(f"Parameters Missing. Call from terminal as \npython3 main.py [input] [output]\n")
    else:
        file_path, new_data = arguments[1], arguments[2]
    etl_helper(file_path, new_data, engine, table_name)


if __name__ == '__main__':
    main()