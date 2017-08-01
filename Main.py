'''
Created on 31/07/2017

@author: olivia
'''
import tweepy
from textblob import TextBlob 
import csv



#initialise keys and tokens from twitter
consumer_key = "jYlLjLrZoz9iZFkwRllh0r9qx"
consumer_secret = "06JeLUhSc4LMz27BMPAVA59aol1aP9i0kgskOf3yARmwOT8Fho"

access_token = "3296540556-P7DiMUNyqu7IzWvMoTF75jXDbzh7z8NgX8tsUj2"
access_token_secret = "Kru1Y6F8BBwmythfuINEApDrUa7SJPhBHLzFLOO5wbBro"

#authenticate with twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#topic to search sentiment
topic = 'Trump'

#function that determiens whether positive or negative
def sentiment_type(analysis):
    if analysis.sentiment[0] > 0:
        return 'Positive'
    else: 
        return 'negative'

#search for tweets
public_tweets = api.search(q = topic, count = 100)

#fields for mean
count = 0
total = 0
#create file to store tweets
with open("twitterSentiment.csv", "wb") as file:
    file.write('tweet, sentiment_label\n')
for tweet in public_tweets:
    count = count + 1
    #Perform sentiment analysis on tweets
    analysis = TextBlob(tweet.text)
    total = total + analysis.sentiment[0]
    #get label of analysis
    file.write('%s,%s\n' % (tweet.text.encode('utf8'), sentiment_type(analysis)))

#get mean of all tweets
mean = total / count
if mean < 0:
    sentiment = 'Negative'
else:
    sentiment = 'Positive'
    
print("Overall %s sentiment towards %s" % (sentiment, topic))


    