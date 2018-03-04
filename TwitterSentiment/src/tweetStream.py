#http://adilmoujahid.com/posts/2014/07/twitter-analytics/
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from textblob import TextBlob

#get credentials
filename="../credential.txt"
cred = {}
with open(filename) as f:
    lines = f.read().splitlines() 
for line in lines:
    splited = line.split(":")
    cred[splited[0]]=splited[1]



#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(cred['consumer_key'], cred['consumer_secret'])
    auth.set_access_token(cred['access_token'], cred['access_token_secret'])
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['psg'])
    

