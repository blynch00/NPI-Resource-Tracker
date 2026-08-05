# Used to store static definitions for file pathing & headers for pandas dataframes.
from sqlalchemy import types
NEW_FILE_NAME = "../data/new_npi.csv"
DEFAULT_DATA_PATH = "../data/npi_data.csv"


DEFAULT_HEADERS =  {
    "first_name": "N/A", 
    "last_name": "N/A", 
    "address": "N/A",
    "state": "XX", 
    "zip": "XXXXX",
    "phone": "XXXXXXXXXX",
    "taxonomy_code": "XXXXXXXXXX"
    }

DATA_CASTS = {
    "npi_code": types.CHAR(10),
    "last_name": types.String(50),
    "first_name": types.String(50),
    "address": types.String(150),
    "state": types.CHAR(2),
    "zip": types.CHAR(5),
    "phone": types.CHAR(10),
    "taxonomy_code": types.CHAR(10)
}

NEW_HEADERS = [
    "npi_code", 
    "first_name", 
    "last_name", 
    "address_1", 
    "address_2",
    "state", 
    "zip", 
    "phone", 
    "taxonomy_code"
    ]

EXTRACTION_TYPES = {
    "npi_code": str, 
    "first_name": str, 
    "last_name": str, 
    "address_1": str, 
    "address_2": str,
    "state": str, 
    "zip" : str, 
    "phone" : str, 
    "taxonomy_code" : str

}
