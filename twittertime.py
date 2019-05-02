import tweepy, time, datetime

#Determines how often you tweet, measured in seconds.
INTERVAL = 60 

#Twitter tokens handled by tweepy
#Insert your keys:
CONSUMER_KEY = '...'
CONSUMER_SECRET = '...'
ACCESS_KEY = '...'
ACCESS_SECRET = '...'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    now = datetime.datetime.now() #Update the time.
    tweet = now.strftime("The time is %H:%M:%S. Better get going!") #Let's fix that string.
    api.update_status(tweet) #Update twitter status.
    time.sleep(INTERVAL) #Now wait!
