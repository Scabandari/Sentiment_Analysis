#!/usr/bin/env python
# coding: utf-8

# Every example we could find online used the exact same file for 
# getting twitter data so we didn't have different examples to compare 
# come up w/ our own so we just used this as is after substituting
# our credentials for twitter


import findspark
findspark.init('/home/ubuntu/spark-2.3.2-bin-hadoop2.7')
import pyspark
from pyspark.sql import SparkSession
import tweepy
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
import socket 
import json


consumer_key = 'tti3dryhC6OeEeI6hEbfPTxOC'
consumer_secret = 'FpkYkwvJPSWpm3nylNauQWFI2QpXq5DNmIZcaCTlLnplnYuJcR'
access_token = '4774958721-kQea74VefOB0fE4wTxV4dtkHZThNauQzzf1fSWl'
access_secret = 'IO8g7oi3AO2GWEhQ1F8eovhSBvaeI76DoSb15QCB4bvbF'


class TweetsListener(StreamListener):
    def __init__(self, csocket):
        self.client_socket = csocket
        
    def on_data(self, data):
        try:
            msg = json.loads(data)
            print(msg['text'].encode('utf-8'))
            self.client_socket.send(msg['text'].encode('utf-8'))
        except BaseException as e:
            print("ERROR", e)
        return True
    
    def on_error(self, status):
        print(status)
        return True


def sendData(c_socket):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    twitter_stream = Stream(auth, TweetListener(c_socket))
    twitter_stream.filter(track=['BTC', 'btc'])


if __name__ == '__main__':
    s = socket.socket()
    host = socket.gethostname()
    port = 5555
    s.bind((host, port))
    print("Listening on port 5555\n")
    s.listen(5)
    c, addr = s.accept()
    
    sendData(c)

