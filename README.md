# **Automated Gold Rate Extractor**

## **Project Overview**

The Automated Gold Rate Extractor is a Python-based automation tool that fetches daily gold prices using an API and stores them automatically in an Excel file. 
This eliminates the need for manually checking rates every day and allows easy trend tracking, visualization, and time-series analysis.

## **Features**

- Daily Automation: Automatically fetches gold rates everyday using a scheduler or .bat script.
- Live API Integration: Retrives live gold prices in USD using the **GoldAPI.io** endpoint.
- Currency Conversion: Converts prices from USD to INR using a predefined exchange rate.
- Historical tracking: Saves daily data into an Excel file for long-term trend analysis.
- Summary Report: Displays the highest, lowest, and average gold prices recorded so far. 

# **Tech Stack**

- Language: Python
- Libraries: requests, pandas, datetime, os
- Data Storage: Excel
- Automation: Windows Task Scheduler

# **How it Works**

1. The script calls **GoldAPI** to fetch real-time gold prices (in USD).
2. Converts the fetched price into INE using the current conversion rate.
3. Logs the Date, USD price, and INR price into **gold_rates.xlsx**
4. If the file exists, it appends new data without duplication.
5. Outputs a short summary of the highest, lowest, and average prices so far.

# **Example Output**

Gold Price Today (INR) : 323397.56799999997

Summary so far:
Highest Prince : 323397.56799999997
Lowest Price : 277561.856
Average Price : 289886.2328

# **Future Enhancements**

- Real-time currency conversion using API integration
- Email or Telegram alerts for daily rates
- Data Visualization dashboard using PowerBI or Streamlit
