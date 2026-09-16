# Used to store static definitions for file pathing & headers for pandas dataframes.
from sqlalchemy import types
from sqlalchemy.sql.type_api import TypeEngine
NEW_FILE_NAME = "../data/new_npi.csv"
DEFAULT_DATA_PATH = "../data/npi_data.csv"


DEFAULT_HEADERS =  {
    "first_name": "XX", 
    "last_name": "XX", 
    "address_1": "XX",
    "address_2": "XX",
    "state": "XX", 
    "zip": "XXXXX",
    "phone": "XXXXXXXXXX",
    "taxonomy_code": "XXXXXXXXXX",
    "city": "XXXXX"
    }

DATA_CASTS = { 
    "npi_code": types.CHAR(10), 
    "last_name": types.VARCHAR(150), 
    "first_name": types.VARCHAR(150), 
    "address_1": types.VARCHAR(150), 
    "address_2": types.VARCHAR(150), 
    "city": types.VARCHAR(150), 
    "state": types.VARCHAR(150), 
    "zip": types.VARCHAR(150), 
    "phone": types.VARCHAR(150), 
    "taxonomy_code": types.VARCHAR(150) 
    }

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
