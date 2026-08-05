import pandas
from sqlalchemy import types
from .config import NEW_FILE_NAME, DATA_CASTS, SQL_TABLE_NAMES

def load_npi_data(chunk, index=0, path_name=NEW_FILE_NAME, engine=None, db_name='npi_data') -> int:
    '''
    
    '''

    added_lines = 0
    try:
        if index == 0:
            added_headers = True
        else:
            added_headers = False
        if engine is None:
            print("Engine is None; CSV Only.")
        else:
            added_lines = chunk.to_sql(name=db_name, con=engine, if_exists='append', method="multi", index=False)
            if added_lines == 0:
                raise ValueError(f"ERROR: No rows were added to SQL DB.")
        chunk.to_csv(path_name, index=False, mode = 'a', header = added_headers)
    except Exception as error_msg:
        raise ValueError(f"ERROR: {error_msg}")
    
    return added_lines