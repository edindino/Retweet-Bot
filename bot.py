import tweepy
import re
from time import sleep
from os import environ

CONSUMER_KEY = environ['45G34PMTKvsS8HgPAIrzMcUPx']
CONSUMER_SECRET = environ['E6mRsQ6n4jEEZZEoyI27jYWFEUPqmHqIDTWNYu76Y8f6aWRMtm']
ACCESS_KEY = environ['1098589546223226883-CyE1GO8LmcWAWhM6UGnj8nrJdQUhZH']
ACCESS_SECRET = environ['nv8X8R2tLCrzbjhxoQHL2oU4vxibW25v2olMipAYP30iq']

api = None
wtf = None

def auth():
	#Authenticating API keys
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	#Calling the api
	global api
	api = tweepy.API(auth)

	#Getting Wtf facts's handle
	global wtf
	wtf = api.get_user("WhatTheFFacts")

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

def print_tweets():
	pids = []
	# score = re.compile(r'[0-9]+\s*\-\s*[0-9]+')

	while True:
		for tweet in api.user_timeline(wtf.screen_name):
			try:
				# Retweet tweets as they are found
				tweet.retweet()
				print(tweet.text)
				sleep(60 * 60 * 24)

			except tweepy.TweepError as e:
				print(e.reason)

def main():
	auth()
	print_tweets()

if __name__ == "__main__":
	main()