import pandas
from .config import DEFAULT_HEADERS


                            # Each chunk is an individual DataFrame
def transform_npi_data(data_frame:pandas.DataFrame) -> pandas.DataFrame:
    '''
    Takes smaller pd dataframe chunks given from the chunk iterator, and cleans/validates
    data. Returns dataframe to be inserted into SQL/CSV file.
    '''
    try: 
        # drop any rows without an NPI number, as NPI is primary key in SQL table.
        data_frame = data_frame.dropna(subset=['npi_code'])
        # drop any duplicate numbers
        data_frame = data_frame.drop_duplicates(subset=["npi_code"])

        data_frame = data_frame.fillna(value=DEFAULT_HEADERS)
    except Exception as error_msg:
        raise error_msg
    #print(data_frame.head(100))
    return data_frame

# if __name__ == '__main__':
#     test_data = pandas.read_csv("test_data/test.csv",sep=',', header=None, names=NEW_HEADERS, skiprows=1)
#     transform_npi_data(test_data)


# Concatenate address_1 and address_2 into a single value
#ata_frame['address'] = data_frame['address_1'] + data_frame['address_2'] + data_frame['city']
# Cast new address as str, then drop the columns used to create the new column.
#data_frame['address'].astype(str)
#ata_frame.drop(columns=['address_1', 'address_2','city'], inplace=True, errors='ignore')
# Fill any missing values with default headers, defined in config.py