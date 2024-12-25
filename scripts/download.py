import os 
import requests
import zipfile
import io
from urllib.request import urlretrieve
import pandas as pd


def get_tlc_raw():
    '''
    Retrieve data of HVFHV from Dec-2023 to May-2024 (6 months)
    '''
    
    # Identify landing data folder
    output_relative_dir = '../data/landing/'
    
    if not os.path.exists(output_relative_dir):
        os.makedirs(output_relative_dir)
        
    data = {2023: [12], 2024: [1,2,3,4,5]}
    
    URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_"#year-month.parquet

    for year in data.keys():
        for month in data[year]:
            month = str(month).zfill(2)
            print(f"Begin month {month} - year {year}")
            # Generating url
            url = f'{URL_TEMPLATE}{year}-{month}.parquet'
            # Generating output location and filename
            output_dir = f"{output_relative_dir}/{year}-{month}.parquet"
            # Downloading
            urlretrieve(url, output_dir) 
            
            print(f"Completed month {month}")
    
    return 0


def get_weather_raw():
    '''
    Retrieve hourly weather data from NOAA (NY City Central Park station) from Dec 2023 to May 2024
    '''
    
    print("Begin weather")
    
    # Reading the csv files
    df_2023 = pd.read_csv('https://www.ncei.noaa.gov/data/global-hourly/access/2023/72505394728.csv')
    df_2024 = pd.read_csv('https://www.ncei.noaa.gov/data/global-hourly/access/2024/72505394728.csv')
    
    # Getting the range from Dec 2023 to May 2024 and concatenate them
    df_2023 = df_2023[df_2023['DATE'] >= '2023-12-01']
    df_2024 = df_2024[df_2024['DATE'] < '2024-06-01'] 
    df = pd.concat([df_2023, df_2024])
    
    # Report_type = FM-15: Retrieving hourly record (At minute 51)
    df = df[df['REPORT_TYPE'] == 'FM-15']
    
    # Storing at landing data folder
    df.to_csv('../data/landing/weather_raw.csv')
    
    print("Completed weather")
    return 0
    
def get_taxi_zones():
    '''
    Retrieving shapefile and zone_lookup
    '''    
    # Creating taxi_zones folder
    if not os.path.exists('../data/taxi_zones/'):
        os.makedirs('../data/taxi_zones/')
        
    # Getting zone lookup csv
    zone = pd.read_csv('https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv')
    zone.to_csv('../data/taxi_zones/zone_lookup.csv')
    
    # Getting shapefile
    url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zones.zip'
    response = requests.get(url)
    zip_file = zipfile.ZipFile(io.BytesIO(response.content))
    zip_file.extractall('../data/taxi_zones/')


# Retrieve the tlc data
get_tlc_raw()
get_weather_raw()
get_taxi_zones()
    

# Create raw folder
if not os.path.exists('../data/raw/'):
        os.makedirs('../data/raw/')
        
# Create curated folder
if not os.path.exists('../data/curated/'):
        os.makedirs('../data/curated/')