import requests
import pandas as pd
from datetime import datetime
import os

#Config
API_KEY = "goldapi-dnpqysmeb2pl0s-io"
BASE_URL = "https://www.goldapi.io/api/XAU/USD"
INR = 83.2
FILE_NAME = "gold_rates.xlsx"

#Fetching gold price
headers = {
    "x-access-token": API_KEY,
    "Content-Type": "application/json"
}


response = requests.get(BASE_URL, headers=headers)

if response.status_code == 200:
    data = response.json()
    gold_price_in_USD = data.get("price")
    gold_price_in_INR = gold_price_in_USD * INR
    today = datetime.today().strftime("%d/%m/%Y")

    #saving to excel

    new_row = {
        "Date" : today,
        "Gold Price (USD)" : gold_price_in_USD,
        "Gold Price (INR)" : gold_price_in_INR

    }

    if os.path.exists(FILE_NAME):
        df = pd.read_excel(FILE_NAME)
        if today not in df["Date"].astype(str).values:
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    else:
        df = pd.DataFrame([new_row])

    df.to_excel(FILE_NAME, index=False)

    #Summary report
    highest = df["Gold Price (INR)"].max()
    lowest = df["Gold Price (INR)"].min()
    average = df["Gold Price (INR)"].mean()

    print(f"Gold Price Today (INR) : {gold_price_in_INR}")
    print("\nSummary so far:")
    print(f"Highest Prince : {highest}")
    print(f"Lowest Price : {lowest}")
    print(f"Average Price : {average}")

else:
    print("Error Fetching Data:", response.status_code,response.text)

