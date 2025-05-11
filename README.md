# Airline Delay Prediction Project

**GitHub Pages Link**: [https://seanzero7.github.io/AirlineDelayML.github.io/](https://seanzero7.github.io/AirlineDelayML.github.io/)

## Overview

By Julia Baratta and Sean Hall

The main objective of our project is to identify the variables that affect flight delays and create a predictive model that will display the probability that a given flight will be delayed based on set characteristics.

A major question we addressed is: does rain and snow affect the likelihood that your flight will be delayed? To tackle this variable, we imported and cleaned datasets from the National Center for Environmental Information that include data on daily precipitation in major US cities. We focused on the ten cities with the largest airports to analyze. We generalized the trend between weather and flight delays to every airport in the US with the assumption that they will behave reasonably similarly to our chosen cities.

## Data Sources

We used the following data sources for our analysis:

- **Flight Data**: The Bureau of Transportation Statistics' On-Time Performance dataset, which contains details on every flight flown in the US from 2013-2023
  - [BTS On-Time Performance Data](https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ&QO_fu146_anzr=b0-gvzr)

- **Weather Data**: National Center for Environmental Information daily summaries for precipitation and snow in major US cities
  - [NCEI Daily Summaries](https://www.ncei.noaa.gov/access/search/data-search/daily-summaries?pageNum=1&startDate=2018-01-03T00:00:00&endDate=2018-01-03T23:59:59&dataTypes=AWND&dataTypes=PRCP&dataTypes=TAVG&bbox=38.030,-122.674,37.520,-122.164)

## Methodology

Our approach consisted of several steps:

1. **Data Collection**: Gathered flight data from BTS and weather data from NCEI
2. **Data Cleaning and Preprocessing**:
   - Filtered for flights between the top 10 US airports
   - Handled missing values (dropped rows with NaN values as they made up <2% of the dataset)
   - Integrated weather data with flight data
   - Defined delay threshold (5 minutes or more) based on statistical analysis

3. **Exploratory Data Analysis**:
   - Analyzed relationships between various features and flight delays
   - Examined historical trends in precipitation, snow, and their correlation with delays
   - Identified the most delayed airlines, airports, and times of year

4. **Machine Learning Model Development**:
   - Built a Random Forest Regression model to predict delay times
   - Used features including:
     - Flight details (departure time, distance, etc.)
     - Weather conditions (snow, precipitation)
     - Temporal features (day of week, month, year)
     - Categorical features (airline, origin/destination airports)

5. **Model Validation**:
   - Implemented a rolling validation approach, training on one year and testing on the next
   - Evaluated using Mean Absolute Error (MAE) and R-squared metrics

## Key Findings

- Our model achieved high predictive accuracy with R-squared values consistently above 0.91 across all test years
- Weather conditions, particularly precipitation, show significant correlation with flight delays
- Mean Absolute Error typically ranges from 5-7 minutes, indicating good predictive performance
- 2016 and 2022 showed less precipitation in New York (correlated with drought periods), affecting delay patterns
- The model was successfully tested on personal flights for validation purposes

## Interesting Observations

- Average delays vary significantly by airline and year
- Snow levels have been decreasing on average over the analyzed period, possibly reflecting climate change
- Certain airports consistently experience more delays regardless of weather conditions
- Major weather events (like the 2016 New York drought) are clearly reflected in the delay data

## Contributors

We collaborated on this project with the following workflow:
- Set up a GitHub Repository to edit and share code
- Met weekly on Thursdays from 12:30 pm - 2:00 pm 
- Worked together as neighbors for additional meetings as needed

## Files in this Repository

- `FinalProject.ipynb`: Main analysis notebook with data processing and ML model
- `MLready.csv`: Processed dataset ready for machine learning
- Various supplementary data files and visualizations

## Future Work

For future iterations of this project, we could:
- Include more airports and a wider range of weather variables
- Implement more sophisticated models like gradient boosting or neural networks
- Add real-time prediction capabilities for current flights


