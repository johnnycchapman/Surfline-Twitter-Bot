# Wrightsville Beach, NC Surfline Twitter Bot 🌊

This bot fetches the daily surf forecast from Surfline and automatically posts it to Twitter at 8 AM EST every day. The script is powered by GitHub Actions, which ensures the bot runs on schedule without manual intervention.

## How It Works
1. Fetches Surf Forecast: Uses the pysurfline API to retrieve wave conditions, sunrise, and sunset times for a specified surf spot.
2. Formats the Forecast: Extracts key details for 8 AM and 2 PM local time (EST) and converts them into a readable tweet.
3. Posts to Twitter: Uses tweepy to authenticate and post the forecast from a Twitter account.
4. Runs Daily at 8 AM EST: GitHub Actions schedules and executes the bot automatically.

## Project Files
* get_surf.py – Fetches and processes surf forecast data.
* post_tweet.py – Formats and posts the tweet.
* dailyschedule.yaml – GitHub Actions workflow file to run the bot daily.
* requirements.txt – Lists required dependencies.

## Setup Instructions
To use this bot, you'll need:

* A Twitter Developer Account with API keys
* A GitHub repository with GitHub Actions enabled
* Secrets stored in GitHub Actions settings for API authentication

## Customization

* Change the Spot ID in post_tweet.py to fetch forecasts for a different surf location.
* Modify the posting time by updating dailyschedule.yaml.

Enjoy automated surf reports! 🌊🤙