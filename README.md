# Google API Data Compilation & Trend Analysis

This project automates the process of compiling data from Google APIs, including the GA4 API for website analytics and Google Trends for trend analysis. It utilizes **Poetry** for dependency management, ensuring smooth installation and usage of the required libraries.
## Features
- **GA4 API Integration**: Fetch detailed day-by-day website analytics, including user sessions, page views, conversions, and engagement metrics.
- **Google Trends Integration**: Analyze search trends over time, for up to 12 months or 3 months, with data exported into CSV for further analysis.
- **Data Export**: Automatically saves both GA4 analytics and Google Trends data into CSV files for easy access and reporting.

## Project Structure

```
/your_project_directory/
├── ga4_detailed_report.py       # Script to fetch GA4 analytics data and save to CSV
├── google_trends_12_months.py   # Script to fetch Google Trends data over the past 12 months
├── google_trends_3_months.py    # Script to fetch Google Trends data over the past 3 months
├── poetry.lock                  # Poetry lock file for dependency management
├── pyproject.toml               # Project configuration file for Poetry
└── README.md                    # Project README file
```

## Setup Instructions

### 1. Install Dependencies
Ensure you have **Poetry** installed for dependency management. Run the following command to install the project dependencies:

```bash
poetry install
```

### 2. Running the Project

#### 2.1 Fetch GA4 Analytics Data
To fetch the GA4 analytics data for your property and export it as a CSV file, run:

```bash
python ga4_detailed_report.py
```

#### 2.2 Fetch Google Trends Data (12 Months)
To fetch Google search trends over the past 12 months, run:

```bash
python google_trends_12_months.py
```

#### 2.3 Fetch Google Trends Data (3 Months)
To fetch Google search trends over the past 3 months, run:

```bash
python google_trends_3_months.py
```
## Dependencies

- **Python 3.x**
- **Poetry** for dependency management
- **Google Analytics Data API**
- **Pytrends** (Google Trends API)

## Future Improvements

- Adding more customizable parameters for the Google Trends API.
- Extend GA4 data fetching to include additional metrics and dimensions.
- Build visualization tools to display trends and analytics results within the script.
