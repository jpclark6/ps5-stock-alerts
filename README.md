# PS5 Stock Alerts from Twitter

I was looking for a PS5 but with the demand and bots it's basically impossible to find one. To give myself the best chance I wrote a script to help me out. This is a python script that sets up a listener using the Twitter API for terms relating to PS5 drops. If it gets one it will play a sound to alert you, and show you the tweet (they usually have a link to the site that the PS5 is in stock).

It's currently fairly liberal with quite a few false positives, but it could be updated to possibly miss a drop or two but have less false positives.

## Requirements

You'll need to snag an API key from twitter. Once you get signed up for their API you'll grab the Bearer token. This is all you'll need, other than python 3.6+.

## Setup

Clone the repo and then cd into the directory.

Setup your virtual environment and requirements. (May need to add 3's to the python and pip commands depending on your environment)

`python -m venv venv`

`pip install -r requirements.txt`

Set up the .env file. Copy the sample and then fill in your token.

`cp sample.env .env`

On the initial run run this command.

`python ps5_stock_alert.py setup`

On any additional runs just use this command without the argument.

`python ps5_stock_alert.py`

## Does it work?

Kind of. You'll still be up against a ton of demand, but this gives you a fighting chance. Or you could just wait a month or two when they're in stock everywhere.