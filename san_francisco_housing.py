# Importing the required libraries and dependencies.
import pandas as pd
import hvplot.pandas
from pathlib import Path


# Using the read_csv function and Path module, create a DataFrame.

sfo_data_df = pd.read_csv(
    Path("sfo_neighborhoods_census_data.csv")
)

# Review the first and last five rows of the DataFrame.
display(sfo_data_df.head(3))
display(sfo_data_df.tail(3))


# Creating a numerical aggregation that groups the data by the year and then averages the results.
housing_units_by_year = sfo_data_df.groupby('year').mean()

# Review the DataFrame
housing_units_by_year


# Create a visual aggregation explore the average gross rent by year using HvPlot.
housing_units_by_year.hvplot.bar(
    x="year",
    y="gross_rent",
    title="Average Gross Rent in San Francisco from 2010 to 2016",
    color="red",
    xlabel="Year",
    ylabel="Gross Rent"
).opts(yformatter='%.0f')

# Group by year and neighborhood and then create a new dataframe of the mean values

prices_by_year_by_neighborhood = sfo_data_df.groupby(by=['year','neighborhood']).mean()

# Review the DataFrame
prices_by_year_by_neighborhood.head()

# Filter out the housing_units
prices_by_year_by_neighborhood = prices_by_year_by_neighborhood.drop(columns=['housing_units'])

# Review the first and last five rows of the DataFrame
display(prices_by_year_by_neighborhood.head())
display(prices_by_year_by_neighborhood.tail())


# Use hvplot to create an interactive line plot of the average price per square foot
prices_by_year_by_neighborhood.hvplot.line(
    x="year",
    y=["sale_price_sqr_foot", "gross_rent"],
    groupby="neighborhood",
    title="Price per square foot and average gross rent 2010 to 2016 in SF per Neighborhood"
)