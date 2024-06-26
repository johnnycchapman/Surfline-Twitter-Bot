import tweepy
import pysurfline
from requests_oauthlib import OAuth1
from get_surf import get_surf_forecast

# Twitter API credentials
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

client = tweepy.Client(BEARER_TOKEN,CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

spot_forecasts = pysurfline.get_spot_forecasts(
    spotId='5842041f4e65fad6a7708a65',
    days=1,
    intervalHours=3,
)

# Initialize Tweepy
auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def post_tweet(tweet_text):
    # Post the tweet
    client.create_tweet(text=tweet_text)

def main():
    # Get surf forecast
    surf_forecast_string = get_surf_forecast('5842041f4e65fad6a7708a65')

    # Tweet text
    tweet = "Today's Forecast:\n" + surf_forecast_string
    
    # Post tweet
    post_tweet(tweet)

    # Print tweet
    print("Tweet posted!", tweet)

if __name__ == "__main__":
    main()
