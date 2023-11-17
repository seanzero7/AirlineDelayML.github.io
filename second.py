import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('airline_data/sample1000df.csv')

#Changing CancellationCodes
df["CancellationReason"] = df["CancellationCode"].replace({'A':"Carrier",'B':"Weather",'C':"National Air System",'D':"Security",np.nan:'No Delay'})
df.drop(columns=['CancellationCode'],inplace=True)

#Changing Airline Name Column
DOT_ID_Airline_df = pd.read_csv('../Desktop/airline_data/L_AIRLINE_ID.csv')
ID_map_dict = dict(zip(DOT_ID_Airline_df['Code'], DOT_ID_Airline_df['Description'].str.split(':').str[0])) 
df['Airline'] = df['DOT_ID_Reporting_Airline'].map(ID_map_dict)
df.drop(columns=['DOT_ID_Reporting_Airline'],inplace=True)

#Cleaning data (Some airlines did NaN on delays when they didn't exist. These are equivalent to a 0 time delay.)
#Also, there are 2% of rows that have NaN values. I looked for a correlation and none existed. This should not affect our data. I will drop these rows. 
fill_columns = ['CarrierDelay','WeatherDelay','NASDelay','SecurityDelay','LateAircraftDelay']
df[fill_columns] = df[fill_columns].fillna(0)
df.dropna(inplace=True)

#Changing DayOfWeek column
DayOfWeek_mapping = {1:'Mon',2:'Tues',3:'Wed',4:'Thurs',5:'Fri',6:'Sat',7:'Sun'}
df['DayOfWeek'] = df['DayOfWeek'].map(DayOfWeek_mapping)

#Fixing OriginAirportID
ForeignKey = pd.read_csv('../Desktop/airline_data/L_AIRPORT_ID.csv')
ForeignKeyDict = dict(zip(ForeignKey['Code'], ForeignKey['Description']))
df['OriginAirport'] = df['OriginAirportID'].map(ForeignKeyDict)
df.drop(columns=['OriginAirportID'],inplace=True)


#Fixing OriginCityMarketID, changing name to OriginArea.
ForeignKey = pd.read_csv('../Desktop/airline_data/L_CITY_MARKET_ID.csv')
ForeignKeyDict = dict(zip(ForeignKey['Code'], ForeignKey['Description']))
df['OriginArea'] = df['OriginCityMarketID'].map(ForeignKeyDict)
df.drop(columns=['OriginCityMarketID'],inplace=True)

#Fixing Months
ForeignKey = pd.read_csv('../Desktop/airline_data/L_MONTHS.csv')
ForeignKeyDict = dict(zip(ForeignKey['Code'], ForeignKey['Description']))
df['Month'] = df['Month'].map(ForeignKeyDict)

#Fixing DestAirportID
ForeignKey = pd.read_csv('../Desktop/airline_data/L_AIRPORT_ID.csv')
ForeignKeyDict = dict(zip(ForeignKey['Code'], ForeignKey['Description']))
df['DestAirport'] = df['DestAirportID'].map(ForeignKeyDict)
df.drop(columns=['DestAirportID'],inplace=True)

#Fixing DestCityMarketID
ForeignKey = pd.read_csv('../Desktop/airline_data/L_CITY_MARKET_ID.csv')
ForeignKeyDict = dict(zip(ForeignKey['Code'], ForeignKey['Description']))
df['DestArea'] = df['DestCityMarketID'].map(ForeignKeyDict)
df.drop(columns=['DestCityMarketID'],inplace=True)



# ####Below is trying to find correlations

# target_columns = ['ArrDelayMinutes', 'DepDelayMinutes']

# # Filter numeric columns only
# numeric_columns = df.select_dtypes(include=['number']).columns

# # Compute correlation matrix for numeric columns
# correlation_matrix = df[numeric_columns].corr()

# # Extract correlations with the target columns
# correlations_with_target = correlation_matrix[target_columns]

# # Display columns with the highest correlation for each target
# for target_column in target_columns:
#     correlated_columns = correlations_with_target[target_column].sort_values(ascending=False)
#     print(f"\nColumns most correlated with '{target_column}':")
#     print(correlated_columns)




#FUN FACTS!!


#Airline with the Most Delays:
most_delayed_airline = df.groupby('Airline')['DepDelayMinutes'].mean().idxmax()
print(f"The airline with the most delays is {most_delayed_airline}.")

#Month with the Most Delays:
month_most_delays = df.groupby('Month')['DepDelayMinutes'].mean().idxmax()
print(f"The month with the most delays is {month_most_delays}.")

#Year with the Most Delays:
year_most_delays = df.groupby('Year')['DepDelayMinutes'].mean().idxmax()
print(f"The year with the most delays is {year_most_delays}.")

#Airport with the Longest Average Taxi Out Time:
airport_longest_taxi_out = df.groupby('OriginAirport')['TaxiOut'].mean().idxmax()
print(f"The airport with the longest average taxi out time is {airport_longest_taxi_out}.")

#Average Arrival Delay by City:
avg_arrival_delay_by_city = df.groupby('DestCityName')['ArrDelayMinutes'].mean().idxmax()
print(f"The city with the highest average arrival delay is {avg_arrival_delay_by_city}.")

#Busiest Airport (Most Flights):
busiest_airport = df['OriginAirport'].value_counts().idxmax()
print(f"The busiest airport (with the most flights) is {busiest_airport}.")

#Month with the Highest Average Airtime:
month_highest_airtime = df.groupby('Month')['AirTime'].mean().idxmax()
print(f"The month with the highest average airtime is {month_highest_airtime}.")

#Most Common Delay Type:
most_common_delay_type = df[['CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay']].idxmax(axis=1).mode().values[0]
print(f"The most common delay type is {most_common_delay_type}.")

#Day of the Week with the Fewest Delays:
day_fewest_delays = df.groupby('DayOfWeek')['DepDelayMinutes'].mean().idxmin()
print(f"The day of the week with the fewest delays is {day_fewest_delays}.")






