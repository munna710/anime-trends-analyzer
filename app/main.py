import schedule
import time
from elasticsearch import Elasticsearch
from scraper import get_anime_tweets

es = Elasticsearch("http://elasticsearch:9200")

def job():
    tweets = get_anime_tweets()
    for tweet in tweets:
        es.index(index="anime_tweets", document=tweet)
        print(f"Stored: @{tweet['user']} - {tweet['sentiment']}")

# Schedule every 5 minutes
schedule.every(5).minutes.do(job)

print("⏱️ Running Anime Twitter Trends Analyzer...")
while True:
    schedule.run_pending()
    time.sleep(1)
