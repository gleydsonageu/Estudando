# -*- coding: utf-8 -*-

import twitter
from twitter import *

OAUTH_TOKEN = '865998132517236736-Bn4F0J8agczPJOSE9CzTOzqkrvuTp75'
OAUTH_SECRET = 'ziX22stOPOkCZi4vQnVLQXOWoUDGeOBaNMu64mDVdxgcq'
CONSUMER_KEY = 'Jk1j59W1pzteRMVy85SRVKQZN'
CONSUMER_SECRET = 'C437hqnxUEhlLfcikKK0aOJjENEDyQ0mhg3xMxt2r9QLZIZK8U'

twitter = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
            CONSUMER_KEY, CONSUMER_SECRET))

#-----------------------------------------------------------------------
# perform a basic search 
# Twitter API docs:
# https://dev.twitter.com/rest/reference/get/search/tweets
#-----------------------------------------------------------------------
def search_tweeter(q, count=100):
		query = twitter.search.tweets(q = "foratemer", result_type = 'recent', locate = "pt", count=count)

#print (query)
#-----------------------------------------------------------------------
# How long did this query take?
#-----------------------------------------------------------------------


#-----------------------------------------------------------------------
# Loop through each of the results, and print its content.
#-----------------------------------------------------------------------
for result in query["statuses"]:
	print( '@%s tweeted: %s' % ( result['user']['screen_name'], result['text'] ) )
#	print (%s @%s %s % (result["created_at"], result["user"]["screen_name"], result["text"])
