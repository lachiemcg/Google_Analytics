import os
import pandas as pd
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest
)

# Set up your environment to authenticate with the service account JSON file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'test-data-435104-25f7d06008c5.json'

# Initialize the GA4 client
client = BetaAnalyticsDataClient()

# Define your GA4 property ID and the date range for the report
property_id = "383145044"
starting_date = "365daysAgo"
ending_date = "yesterday"

# Build the API request for maximum detail day-by-day
request = RunReportRequest(
    property=f"properties/{property_id}",
    dimensions=[
        Dimension(name="date"),
        Dimension(name="landingPagePlusQueryString"),
        Dimension(name="sessionSource"),
        Dimension(name="sessionMedium"),
        Dimension(name="deviceCategory"),
        Dimension(name="country"),
        Dimension(name="browser"),
        Dimension(name="eventName")
    ],
    metrics=[
        Metric(name="sessions"),
        Metric(name="totalUsers"),
        Metric(name="screenPageViews"),
        Metric(name="eventCount"),
        Metric(name="conversions"),
        Metric(name="averageSessionDuration"),
        Metric(name="bounceRate"),
        Metric(name="engagementRate"),
        Metric(name="newUsers")
    ],
    date_ranges=[DateRange(start_date=starting_date, end_date=ending_date)]
)

# Fetch the report data from GA4
response = client.run_report(request)

# Function to convert the response data into a Pandas DataFrame
def query_data(api_response):
    dimension_headers = [header.name for header in api_response.dimension_headers]
    metric_headers = [header.name for header in api_response.metric_headers]
    
    # Collect rows of data
    rows = []
    for row in api_response.rows:
        row_data = [dimension_value.value for dimension_value in row.dimension_values]
        row_data += [metric_value.value for metric_value in row.metric_values]
        rows.append(row_data)
    
    # Combine headers (dimensions + metrics)
    headers = dimension_headers + metric_headers
    
    # Create a DataFrame with the rows and headers
    df = pd.DataFrame(rows, columns=headers)
    return df

# Convert API response to a DataFrame
final_data = query_data(response)

# Export the DataFrame to a CSV file
final_data.to_csv('ga4_detailed_report_Mobilise_Website.csv', index=False)
print("Data exported to ga4_detailed_report.csv")
