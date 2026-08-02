import pandas
import os
FILE_NAME = "new_npi.csv"

# Check if file already exists, deleting it if so
file_exists = os.path.exists(FILE_NAME)

if file_exists:
    try:
        os.remove(FILE_NAME)
    except Exception as e:
        print(f"File deletion error. {e}")
        pass

new_headers = [
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

defaults = {
    "First Name": "N/A", 
    "Last Name": "N/A", 
    "Address 1" : "N/A", 
    "Address 2": "N/A", 
    "City" :"NULL", 
    "State": "QQ", 
    "Zip Code": "80503",
    }

data = pandas.read_csv(
    "npi_data.csv",
    sep = ',', 
    skiprows=1,
    header = None,
    names = new_headers,
    dtype = {"NPI":str, "Zip Code": str, "Phone Number": str},
    chunksize = 500000,
    usecols = [0,5,6,20,21,22,23,24,26,47]
    ) 

total_written = 0
for i, chunk in enumerate(data):
    total_written += len(chunk)
    print(f"{len(chunk)} rows; {total_written} written.")
    chunk = chunk.fillna(value=defaults)
    #chunk = chunk.dropna(subset=['NPI'])
    chunk.to_csv(FILE_NAME, index=False, mode = 'a', header =  (i==0))
    
print(f"FINISHED: {total_written} lines.")