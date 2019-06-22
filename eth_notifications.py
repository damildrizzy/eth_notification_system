import requests
import time
from datetime import datetime
ETH_PRICE_THRESHOLD = 350

eth_api_url = 'https://api.coingecko.com/api/v3/coins/ethereum'
webhook_api_url = 'https://maker.ifttt.com/trigger/{}/with/key/bdKj2SFLeSezJPEYBvcgG0XDfVafJIxETmpUFHXAh4-'

def get_latest_eth_price():
    response = requests.get(eth_api_url)
    response_json = response.json()
    return float(response_json['market_data']['current_price']['usd'])


def post_ifttt_webhook(event, value):
    data = {'value1':value}
    ifttt_event_url = webhook_api_url.format(event)
    requests.post(ifttt_event_url, json=data)

def format_eth_history(eth_history):
    rows = []
    for eth_price in eth_history:
        date = eth_price['date'].strftime('%d.%m.%Y %H:%M')  # Formats the date into a string: '24.02.2018 15:09'
        price = eth_price['price']
        # <b> (bold) tag creates bolded text
        row = '{}: $<b>{}</b>'.format(date, price)  # 24.02.2018 15:09: $<b>10123.4</b>
        rows.append(row)

    # Use a <br> (break) tag to create a new line
    return '<br>'.join(rows)  # Join the rows delimited by <br> tag: row1<br>row2<br>row3

def main():
    eth_history = []
    while True:
        price = get_latest_eth_price()
        date = datetime.now()
        eth_history.append({'date': date, 'price': price})

        #send emergency notification
        if price > ETH_PRICE_THRESHOLD:
            post_ifttt_webhook('Eth_Price_Emergency', price)

        #send telegram update
        if len(eth_history) == 5:
            post_ifttt_webhook('Eth_Price_Update', 
                               format_eth_history(eth_history))

            #reset history
            eth_history = []

        # Sleep for 5 minutes 
        time.sleep(5 * 10)




if __name__ == "__main__":
    main()
