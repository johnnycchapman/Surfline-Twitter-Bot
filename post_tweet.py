import os
import tweepy
from get_surf import get_surf_forecast

# Load API credentials from environment variables
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# Initialize Tweepy Client (v2 API)
client = tweepy.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

def post_tweet(tweet_text):
    """Posts a tweet using Tweepy Client API."""
    try:
        client.create_tweet(text=tweet_text)
        print("Tweet posted successfully!")
    except Exception as e:
        print(f"Error posting tweet: {e}")

def main():
    """Fetches surf forecast and tweets it."""
    spot_id = '5842041f4e65fad6a7708a65'  # Default Spot ID
    surf_forecast_string = get_surf_forecast(spot_id)

    if not surf_forecast_string:
        print("No forecast available.")
        return

    tweet = f"Today's Surf Forecast:\n{surf_forecast_string}"
    post_tweet(tweet)

if __name__ == "__main__":
    main()
