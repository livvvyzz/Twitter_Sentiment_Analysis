'''
Created on 31/07/2017

@author: olivia
'''
import tweepy
from textblob import TextBlob 

#initialise keys and tokens from twitter
consumer_key = "jYlLjLrZoz9iZFkwRllh0r9qx"
consumer_secret = "06JeLUhSc4LMz27BMPAVA59aol1aP9i0kgskOf3yARmwOT8Fho"

access_token = "3296540556-P7DiMUNyqu7IzWvMoTF75jXDbzh7z8NgX8tsUj2"
access_token_secret = "Kru1Y6F8BBwmythfuINEApDrUa7SJPhBHLzFLOO5wbBro"

#authenticate with twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#search for tweets
public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    
    #Perform sentiment analysis on tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
    