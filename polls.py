import tweepy
import config
import random


def create_poll():
    client = tweepy.Client(consumer_key=config.API_KEY,
                           consumer_secret=config.API_SECRET,
                           access_token=config.ACCESS_TOKEN,
                           access_token_secret=config.ACCESS_TOKEN_SECRET)

    polls = ['Have you been to this brewery before?', 'If you have not been to this brewery would you now consider it?',
             'Do you like the idea of BrewBot?']

    value = random.choice(polls)

    client.create_tweet(text=f'{value}', poll_duration_minutes=90, poll_options=['Yes', 'No'])
