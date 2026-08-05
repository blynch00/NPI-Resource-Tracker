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

SQL_TABLE_NAMES = {
    "NPI": "npi_code",
    "First Name": "first_name",
    "Last Name": "last_name",
    "State": "state",
    "Address": "address",
    "Zip Code": "zip",
    "Phone Number": "phone",
    "Taxonomy Code": "taxonomy_code"
}

NEW_HEADERS = [
    "NPI", 
    "First Name", 
    "Last Name", 
    "Address 1", 
    "Address 2", 
    "City", 
    "State", 
    "Zip Code",
    "Phone Number", 
    "Taxonomy Code"
    ]

