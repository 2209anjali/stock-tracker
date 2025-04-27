import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_key = #https://www.alphavantage.co/
news_key = #https://newsapi.org/

account_id = #https://console.twilio.com/
account_token = #https://console.twilio.com/

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

stock_info = {
    "function": "TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":stock_key

}
response = requests.get(STOCK_ENDPOINT, params=stock_info)
data = response.json()["Time Series (Daily)"]
datalist = [value for (key, value) in data.items()]
yes_closing_pr = datalist[0]["4. close"]
print(yes_closing_pr)

#TODO 2. - Get the day before yesterday's closing stock price

bef_yes_closing_pr = datalist[1]["4. close"]
print(bef_yes_closing_pr)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

diff = abs(float(yes_closing_pr) - float(bef_yes_closing_pr))
print(diff)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

diff_percent = diff/float(yes_closing_pr)*100
print(diff_percent)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if diff_percent > 5:
    news_info = {
        "apikey": news_key,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_info)
    art = news_response.json()["articles"]
    print(art)

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    #TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    #updated todo 5
    #TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    req_articles = art[:3]
    print(req_articles)


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
        #to send a separate message with each article's title and description to your phone number.

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    news_list = [f"Headline:{art['title']}.\nBrief: {art['url']}"for art in req_articles]
    print(news_list)

    #TODO 9. - Send each article as a separate message via Twilio.

    client = Client(account_id,account_token)

    for art in news_list:
        msg = client.messages.create(
            body=art,
            from_= " GET FROM #https://console.twilio.com/",
            to="enter your no")
#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

