Hello World! By Julia Baratta and Sean Hall

The main objective of our project is to identify the variables that affect flight delays and create a predictive model that will display the probability that a given flight will be delayed based on set characteristics.

 

A major question we would like to answer is: does rain and snow affect the likelihood that your flight will be delayed? To tackle this variable, we chose to import and clean datasets from the National Center for Environmental Information that include data on daily precipitation in major US cities across the globe. We chose the ten cities with the largest airports to analyze. We hope to generalize the trend between weather and flight delays to every airport in the US with the assumption that they will behave reasonably similarly to our chosen cities.

 

Here's some links to where we got this data.

 
https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ&QO_fu146_anzr=b0-gvzr

https://www.ncei.noaa.gov/access/search/data-search/daily-summaries?pageNum=1&startDate=2018-01-03T00:00:00&endDate=2018-01-03T23:59:59&dataTypes=AWND&dataTypes=PRCP&dataTypes=TAVG&bbox=38.030,-122.674,37.520,-122.164

 

Discussion of our supplementary datasets:

Large airports may be more equipped to handle storms and weather due to their robust infrastructure, leading to an inaccuracy within our model to predict delays in a variety of airport sizes. However, one could argue that the size of an airport has little effect on an individual plane’s ability to takeoff or land in unsafe conditions. Additionally, top-ten US airports will have the largest dataset of delayed and on-time flights, leading to a greater statistical significance. Finally, top-ten airports necessarily serve more people than any other grouping of ten airports. This means that a model accurate to these airports will have the largest probability of being correct and useful for any given flyer. For these reasons, we think that our supplementary datasets are useful in the goal of this project.

 

Additional cleanup and trend analysis:

Our goal is to create a model that considers many variables, not just weather. To attack this goal, we further tidied and analyzed our original dataset which contains details on every flight flown in the US. Below, you can see that we dropped unnecessary columns, and made the decision to delete rows with NaN values in them. This decision was informed by analysis of the relevant rows which we believe contain values that are missing at completely random. Additionally, they made up <2% of the dataset.

Collaboration Plan: 
We are going to set up a GitHub Repository to edit and share code
We will meet once a week on Thursdays from 12:30 pm - 2:00 pm 
We are neighbors so we can meet more frequently if needed. 


