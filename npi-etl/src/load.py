import pandas
from sqlalchemy import types
from .config import NEW_FILE_NAME, DATA_CASTS


def load_npi_data(chunk:pandas.DataFrame, index=0, path_name=NEW_FILE_NAME, engine=None, table_name='providers') -> int:
    '''
    Responsible for loading transformed columns into SQL table & csv file. If SQLAlchemy
    engine is None, only the csv file is written to.
    '''
    # Added_lines will only change from 0 if engine exists + SQL Table is written to.
    added_lines = 0
    try:
        # Headers used for csv file.
        if index == 0:
            added_headers = True
        else:
            added_headers = False
        if engine is None:
            print("Engine is None; CSV Only.")
        else:
            # Returns number of rows inserted into SQL table
            added_lines = chunk.to_sql(
                name=table_name, 
                con=engine, 
                # Casts columns to match MySQL table constraints, i.e. CHAR(2) 
                dtype=DATA_CASTS,
                if_exists='append',
                # method='multi' used to make inserts more efficient
                method="multi",
                chunksize=5_000,
                index=False
                )
    # If the SQL table should be written to, but to_sql returned 0, ValueError is raised,
            if added_lines == 0:
                raise ValueError(f"ERROR: No rows were added to SQL DB.")
        # Write to csv; append header if first chunk, and append otherwise.
        chunk.to_csv(path_name, index=False, mode = 'a', header = added_headers)
    except Exception:
        print("rip")
    
    return added_lines