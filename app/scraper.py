import snscrape.modules.twitter as sntwitter
from transformers import pipeline
import ssl
import certifi
import os

sentiment_pipeline = pipeline("sentiment-analysis")


# Set certifi as the cert location
os.environ['SSL_CERT_FILE'] = certifi.where()

def get_anime_tweets(query="#anime", max_tweets=10):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= max_tweets:
            break
        sentiment = sentiment_pipeline(tweet.content)[0]
        tweets.append({
            "id": tweet.id,
            "user": tweet.user.username,
            "text": tweet.content,
            "date": tweet.date.isoformat(),
            "sentiment": sentiment["label"],
            "score": sentiment["score"]
        })
    return tweets
