import tweepy
from tweepy import OAuthHandler

consumer_key="c4a1m0vAFXe6NlmDsbOaRuvbc"
consumer_secret="gX5gt5CVfP5AnZpj2D52vJdYrqqeEaPeMblw2yhEMnmPKCnAfh"
access_token="1339310466-Kx24jNGM7jb3R4MnuBqjFHCJoGmyuenCiYbrux6"
access_token_secret="xNeNC46Uee1RINFb2tpOx7yYe74KmXMSdcVYuDjexAQjS"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#Cursor(api.home_timeline)
#for tweet in Cursor(api.home_timeline).items(200):
#    process_status(tweet)

home_tweets = api.home_timeline(count=40)
#tweets_entity = api.show
for tweet in home_tweets:
        print tweet.user.name 
        print tweet.text
        print tweet.created_at
        print tweet.source	
        print "twitter status entities: "        
        for url in tweet.entities['urls']:                
                print url['url']
                print tweet.user.profile_image_url
                print 
