import io
import tweepy
import csv
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#import nltk
#nltk.download('stopwords');

def clean_tweet(tweet):
    '''
    Utility function to clean the text in a tweet by removing 
    links and special characters using regex.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

#OATH
consumer_key = 'tti3dryhC6OeEeI6hEbfPTxOC'
consumer_secret = 'FpkYkwvJPSWpm3nylNauQWFI2QpXq5DNmIZcaCTlLnplnYuJcR'
access_token = '4774958721-kQea74VefOB0fE4wTxV4dtkHZThNauQzzf1fSWl'
access_token_secret = 'IO8g7oi3AO2GWEhQ1F8eovhSBvaeI76DoSb15QCB4bvbF'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#IMPORT STOP WORDS
stop_words = set(stopwords.words('english'))

#SEARCH INFO
search_text = "#BTC"
search_result = api.search(search_text, lang="en", count=100, result_type="mixed", until="2018-11-15")
search_result = search_result + api.search(search_text, lang="en", count=100, result_type="mixed", until="2018-11-12")
#DO THE WORK
for tweet in search_result:
   words = clean_tweet(tweet.text.encode('utf-8')).split()
   for word in words:
        if (not word in stop_words) and not word.isdigit():
                appendFile=open('words.txt', 'a')
                appendFile.write("\n"+word)
                appendFile.close()
