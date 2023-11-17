import pandas as pd
import time 

start_year = 2013
end_year = 2023  

selected_columns = ['Year', 'Month', 'DayofMonth', 'DayOfWeek', 'DOT_ID_Reporting_Airline',
      'OriginAirportID',
     'OriginCityMarketID', 'OriginCityName',
       'OriginStateName', 
       'DestAirportID', 'DestCityMarketID',
       'DestCityName', 'DestStateName',
    'CRSDepTime', 'DepTime', 'DepDelayMinutes',
     'TaxiOut',
      'TaxiIn', 'CRSArrTime', 'ArrTime',
       'ArrDelayMinutes',
       'Cancelled', 'CancellationCode', 'Diverted', 'CRSElapsedTime',
       'ActualElapsedTime', 'AirTime', 'Distance', 
       'CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay',
       'LateAircraftDelay', ] 

start_time = time.time()
# Define the range of years you want to read data for
start_year = 2013
end_year = 2023  # Adjust the end year as needed

# Initialize an empty list to store DataFrames
data_frames = []

# Loop through the years and months and read data into DataFrames
for year in range(start_year, end_year + 1):
    max_month = 12 if year != 2023 else 8
    for month in range(1, max_month + 1):
        file_path = f"airline_data/{year}/On_Time_Reporting_Carrier_On_Time_Performance_1987_present_{year}_{month}/On_Time_Reporting_Carrier_On_Time_Performance_(1987_present)_{year}_{month}.csv"
        try:
            df = pd.read_csv(file_path, usecols=selected_columns)
            data_frames.append(df)
        except FileNotFoundError:
            print(f"File not found for {year}-{month}")
            
# Concatenate all the DataFrames into one
final_df = pd.concat(data_frames, ignore_index=True)

# Now final_df contains data from all specified years and months with the selected columns
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

with open('airline_data/FullAirline.csv','w'):
    pass

final_df.to_csv('FullAirline.csv',index=False)

print(final_df.shape)