import tweepy
import sys 
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import threading
import time
import json
from tweepy import Stream


#apps streaming = @SCsadangserang
consumer_key='t09Bj4zaKIjOOgJyCakJoQXPX'
consumer_secret='pmTmQ0ggVzg72iofoN6PMLuWr8s3TTA4xYVbw7a0dNNTGRS7iH'
access_token='2910905401-6HhFWEqG4QsypFRgloSa6VM5pMfleH91sEw7T5r'
access_token_secret='DLVzAUIMDvOj5i16yZsqaL3Ie4F2usdGvcpU9EwQHHRfc'

#auth method
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#autentikasi
api = tweepy.API(auth)

#list accounts dan id-nya
accnts = []
accntIDs = []

accnts.append('@ridwankamil')
accntIDs.append(80323736)

accnts.append('@odedmd')
accntIDs.append(1319572040)

accnts.append('@2Serang')
accntIDs.append(1903129470)

accnts.append('@diskominfobdg')
accntIDs.append(1933882213)


accnts.append('@persibofficial')
accntIDs.append(174362532)

accnts.append('@simamaung')
accntIDs.append(80528320)

accnts.append('@officialvpc')
accntIDs.append(114668227)


accnts.append('@infobandung')
accntIDs.append(74081981)

accnts.append('@infobdg')
accntIDs.append(101494663)

accnts.append('@lokerbdg')
accntIDs.append(136212383)


tweetCount = 30

#list tweets dari account
accntsTweets = []

#list keywords
keywords = []
keywords.extend(['lowongan', 'pekerjaan'])
keywords.extend(['persib', 'bobotoh', 'viking'])
keywords.extend(['pembangunan', 'mou', 'anggaran', 'ground breaking'])
keywords.extend(['perda', 'uu', 'undang', 'izin'])
keywords.extend(['sadang serang'])

hashtags = []
hashtags.extend(['#loker', '#lowker', '#persibday'])

#list tweets dari filter
keywordsTweets = [[] for x in range(len(keywords))]
hashtagsTweets = [[] for x in range(len(hashtags))]


#metode untuk stream seach keyword
class StdOutListener(StreamListener):
		def on_data(self, data):
			print data
			return True

		def on_error(self, status):
			print status

#search per keyword (blm diparse)


#home_tweets = api.home_timeline(count=2)
#metode ambil tweet dari account dan masukin hasilnya ke accntsTweets
def getAccntsTweets ():
    for accntID in accntIDs:
        print "fetching new account"
        accntsTweets.append(api.user_timeline(user_id=accntID, count = tweetCount))

#metode filter tweet dari account dan masukin hasilnya ke keywordsTweets
def getFiltersTweets ():
    for accntTweets in accntsTweets:
        print "filtering new account"
        tweetContainer = ""
        for tweet in accntTweets:
            for i in xrange(len(keywords)):
                print "filtering for ", keywords[i]
                if (tweet.text.lower().find(keywords[i]) >= 0):
                    keywordsTweets[i].append(tweet)
                    print "     found from ", tweet.text
            
            for hashtag in tweet.entities['hashtags']:
                for j in xrange(len(hashtags)):
                    print "filtering for ", hashtags[j]
                    if (hashtag['text'].lower().find(hashtags[j]) >= 0):
                        hashtagsTweets[j].append(tweet)
                        print "     found from ", tweet.text

#metode save tweet dari array tweet ke file
def saveTweets (tweetArrays, fileNames):
    for i in xrange(len(tweetArrays)):
        tweetArray = tweetArrays[i]
        print "saving new file"
        tweetContainer = ""
        for tweet in tweetArray:
            tweetContainer += 'Name: ' + tweet.user.name + '\n' + '\r'
            tweetContainer += 'Username: @' + tweet.user.screen_name + '\n' + '\r'
            tweetContainer += 'Status: ' + tweet.text + '\n' + '\r'
            
            createdAt = tweet.created_at         
            tweetContainer += 'CreatedAt: ' + createdAt.strftime('%a, %b, %d, %H:%M:%S +0000 %Y') + '\n' + '\r'
            
            tweetContainer += 'Link: '
            for url in tweet.entities['urls']:
                tweetContainer += url['url']
            tweetContainer += '\n' + '\r'

            tweetContainer += 'Hashtags: '
            for hashtags in tweet.entities['hashtags']:
                tweetContainer += '#' + hashtags['text'] + '\n' + '\r'
            tweetContainer += '\n' + '\r'
            
            tweetContainer += 'ProfilePic:' + tweet.user.profile_image_url + '\n' + '\r'
            tweetContainer += 'userID:' + tweet.user.id_str + '\n' + '\r'

            tweetContainer += '-----------------------------------' + '\n' + '\r'
            
        f = open(fileNames[i] + '.txt', 'w')
        f.write(tweetContainer.encode('utf8'))
        i+=1
        
    print "DONE"

# -----MULAI PANGGIL FUNCTION-----

def fetchTweet():
    print "start fetching"
    getAccntsTweets()
    #accntsTweets.append(api.user_timeline(user_id=136212383, count = tweetCount))
    #accntsTweets.append(api.user_timeline(user_id=1319572040, count = tweetCount))

    saveTweets(accntsTweets, accnts)
    getFiltersTweets()
    saveTweets(keywordsTweets, keywords)
    saveTweets(hashtagsTweets, hashtags)

fetchTweet()                  
threading.Timer(240, fetchTweet).start()
