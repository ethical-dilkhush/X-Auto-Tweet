import tweepy
import time
from dotenv import load_dotenv
import os
import schedule
import sqlite3
# Load API keys from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
# Tweepy Client (v2)
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)
# Tweepy API v1.1 (for media uploads)
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#fetech record from db
def fetch_tweets_from_db():
    """Fetch tweet text and image paths from the database"""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Fetch text and image from database
    cursor.execute("SELECT text, image FROM entries WHERE text IS NOT NULL AND image IS NOT NULL")
    tweets = cursor.fetchall()
    conn.close()
    return tweets

def post_tweet(message, image_path=None):
    try:
        if image_path:
            media = api.media_upload(image_path)  # Upload image
            client.create_tweet(text=message, media_ids=[media.media_id])
        else:
            client.create_tweet(text=message)

        print(f"Tweet posted: {message}")
    except tweepy.TweepyException as e:
        print(f"Error posting tweet: {e}")

# List of (message, image) tuples
tweets = fetch_tweets_from_db()

# Post tweets every 1 hour (3600 seconds)
for message, image in tweets:
    try:
        post_tweet(message, image)
        time.sleep(20)  # Wait before posting next tweet
    except KeyboardInterrupt:
        print("\nBot stopped by user.")
        break
