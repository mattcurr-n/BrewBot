import tweepy
import config


def create_follow_request():
    client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

    followers = client.get_users_followers(config.user_id)

    #tweepy.API.create_friendship(followers)

    print(followers)
