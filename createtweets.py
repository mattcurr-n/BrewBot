import tweepy
import config
import requests
import json
import time


def create_tweets():
    client = tweepy.Client(consumer_key=config.API_KEY,
                           consumer_secret=config.API_SECRET,
                           access_token=config.ACCESS_TOKEN,
                           access_token_secret=config.ACCESS_TOKEN_SECRET)

    r = requests.get(url='https://api.openbrewerydb.org/breweries/random')

    json_string = r.text

    Brewery = json.loads(json_string)

    Brewname = Brewery[0]['name']
    Brewcity = Brewery[0]['city']
    Brewstate = Brewery[0]['state']
    Brewstreet = Brewery[0]['street']
    Brewweb = Brewery[0]['website_url']

    client.create_tweet(text=f'The Brewery of the day is {Brewname}')

    time.sleep(160)

    if Brewcity is None:
        client.create_tweet(text=f'This brewery is located in {Brewstate} on {Brewstreet}')
    elif Brewstate is None:
        client.create_tweet(text=f'This brewery is located in {Brewcity} on {Brewstreet}')
    elif Brewstreet is None:
        client.create_tweet(text=f'This brewery is located in {Brewcity},{Brewstate}')
    else:
        client.create_tweet(text=f'This brewery is located in {Brewcity},{Brewstate} on {Brewstreet}')

    time.sleep(160)

    if Brewweb is None:
        client.create_tweet(text='I could not find a website for this Brewery')
    else:
        client.create_tweet(text=f'Find out more about this brewery at their website {Brewweb}')