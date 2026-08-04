import pandas
from .config import NEW_FILE_NAME

def load_npi_data(chunk:pandas.DataFrame, index:int=0, path_name=NEW_FILE_NAME) -> int:

    added_lines = len(chunk)
    try:
        if index == 0:
            added_headers = True
        else:
            added_headers = False
        chunk.to_csv(path_name, index=False, mode = 'a', header = added_headers)
    except Exception as e:
        raise ValueError(f"ERROR: {e}")
    
    return added_lines