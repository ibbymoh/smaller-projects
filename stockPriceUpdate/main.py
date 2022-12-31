import requests
from datetime import date ,timedelta
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api_key = " UUOO5IFSKBF2JHZI"
news_api_key = "ff6caae84f274dbb90eb77114adfff64"



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


#step 1

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={stock_api_key}"
r = requests.get(url)
data = r.json()

today = date.today()

yesterday = str(today - timedelta(1))
day_before = str(today - timedelta(2))

yesterday_close = float(data['Time Series (Daily)'][yesterday]['4. close'])
day_before_close = float(data['Time Series (Daily)'][day_before]['4. close'])

ratio_change = yesterday_close/day_before_close

if ratio_change > 1.01 or ratio_change < 0.99:
    if ratio_change < 1:
        percentage_change =  100*abs(ratio_change-1)
        message = f"Tesla 🔻{round(percentage_change,2)}"
    elif ratio_change > 1:
        percentage_change = 100 * abs(ratio_change - 1)
        message = f"Tesla🔺{round(percentage_change,2)}"

    r = requests.get(f"https://newsapi.org/v2/everything?q={STOCK}&from={yesterday}&sortBy=popularity&apiKey={news_api_key}")
    results = r.json()
    articles = [{"title": results["articles"][i]["title"],"description": results["articles"][i]["description"]}  for i in range (1,4)]

    body_text = f"{message}%\nHeadline: {articles[0]['title']}\nBrief: {articles[0]['description']}"

    account_sid = "AC7e0f277ef5f6bc3e469f5f71dae08851"
    auth_token = "8e3937514ff733ceffd2f4d72db71a96"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                  body= body_text,
                                  from_='+16812022991',
                                  to='+201097834536'
                              )


