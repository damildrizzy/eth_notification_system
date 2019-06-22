#Ethereum Price Notification System

This Repo includes a python script that returns the lates prices of ethereum and also notifies me when the price is above a certain threshold. I used the popular automation website IFTTT. IFTTT (“if this, then that”) is a web service that bridges the gap between different apps and devices.
I created two IFTTT applets: One for emergency notification when  price falls under a certain threshold; and
another for regular Telegram updates on the Ethereum price.
Both will be triggered by the Python script which will consume the data from the Coingecko API.