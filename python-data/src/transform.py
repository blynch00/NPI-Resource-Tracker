import pandas
from pandas.io.parsers.readers import TextFileReader
from .config import DEFAULT_HEADERS, NEW_HEADERS


                            # Each chunk is an individual DataFrame
def transform_npi_data(data_frame:pandas.DataFrame) -> pandas.DataFrame:
    '''
    Given chunks of data from extract.py, perform data validation in DataFrame, then give to load.py to load into SQL DB.
    '''
    try: 
        data_frame = data_frame.dropna(subset=['NPI'])
        data_frame = data_frame.fillna(value=DEFAULT_HEADERS)
        data_frame = data_frame.drop_duplicates(subset=["NPI"])
    except Exception as error_msg:
        raise error_msg
    print(data_frame.head(100))
    return data_frame

if __name__ == '__main__':
    test_data = pandas.read_csv("test_data/test.csv",sep=',', header=None, names=NEW_HEADERS, skiprows=1, dtype = {"NPI":str, "Zip Code": str, "Phone Number": str})
    transform_npi_data(test_data)