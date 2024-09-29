from pytrends.request import TrendReq
import pandas as pd

# Initialize pytrends
pytrends = TrendReq(geo='AU', tz=360)

# Set up the search term
kw_list = ["YOUR_TREND"]

# Build the payload to get daily data for the last 3 months
pytrends.build_payload(kw_list, cat=0, timeframe='today 3-m', geo='AU', gprop='')

# Get the interest over time data
data = pytrends.interest_over_time()

# Save the data to a CSV file
data.to_csv('YOUR_TREND')

# Load the data for analysis
df = pd.read_csv('YOUR_TREND')

# Inspect the data
print(df.head())

