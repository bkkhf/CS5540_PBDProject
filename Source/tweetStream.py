'''
Created by Balachandar Kulala
This code used to collect the tweet streams using tweepy  module API and writes into the json file.
'''

from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
 
consumer_key = 't4Di3jSU4SLSt1fF19TXCmmJJ'
consumer_secret = 'rBaC14B4Y8qF7PGN45WaEB7Gqmj7mxvBZRD86EL4dKgw0conmK'
access_token = '432443157-WjFlF8SXa3fS8cnA9kbcFosSL8D2WUAcsyG8JWRF'
access_secret = '5kOfEwceBKh9QTOxGdBK36I6STQAhMYdxYlGhB65FFCPk'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('sample.json', 'a') as f:
                f.write(data.encode('utf-8'))
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True


twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#'])