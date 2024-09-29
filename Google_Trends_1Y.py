from pytrends.request import TrendReq
import pandas as pd

# Initialize pytrends
pytrends = TrendReq(geo='AU', tz=360)

# Set up the search term
kw_list = ["homelessness"]

# Build the payload and get the interest over time
pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='AU', gprop='')
data = pytrends.interest_over_time()

# Save the data to a CSV file
data.to_csv('homelessness_trends_aus.csv')

# Load the data for analysis
df = pd.read_csv('homelessness_trends_aus.csv')

# Inspect the data
print(df.head())
