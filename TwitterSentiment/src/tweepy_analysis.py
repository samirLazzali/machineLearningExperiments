#!/usr/bin/env python
# -*- coding: utf-8 -*-
#pip install tweepy
import tweepy
from textblob import TextBlob

#get credentials
filename="../credential.txt"
cred = {}

with open(filename) as f:
    lines = f.read().splitlines() 
for line in lines:
	splited = line.split(":")
	cred[splited[0]]=splited[1]

auth = tweepy.OAuthHandler(cred['consumer_key'], cred['consumer_secret'])
auth.set_access_token(cred['access_token'], cred['access_token_secret'])

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('vero')


def tweetAnalyser(tweet):
    analysis = TextBlob(tweet.text)
    if(analysis.sentiment.polarity != 0 and analysis.sentiment.subjectivity != 0):
    	#print(tweet.text)
    	return [analysis.sentiment]


tweetsSentiments = []
for tweet in public_tweets:
	tmpSentiment = tweetAnalyser(tweet)
	if tmpSentiment:
		tweetsSentiments.append(tweetAnalyser(tweet))
    #Step 4 Perform Sentiment Analysis on Tweets
print tweetsSentiments


#Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself

