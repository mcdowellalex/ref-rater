import os
from requests_oauthlib import OAuth1Session
# import tweepy
import json

consumer_key = 'juouDAV69bmzUVON7S0XvB6oC'  # Add your API key here
consumer_secret = 'ovNWl0wPAA123QcrVgq7fFQbP4O0lN1OXHBvHu473WdiXDf3lS'  # Add your API secret key here


params = {"q": "#blm", 'count': 2}

# Get request token
request_token_url = "https://api.twitter.com/oauth/request_token"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)
fetch_response = oauth.fetch_request_token(request_token_url)
resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')
print("Got OAuth token: %s" % resource_owner_key)

# # Get authorization
base_authorization_url = 'https://api.twitter.com/oauth/authorize'
authorization_url = oauth.authorization_url(base_authorization_url)
print('Please go here and authorize: %s' % authorization_url)
verifier = input('Paste the PIN here: ')

# # Get the access token
access_token_url = 'https://api.twitter.com/oauth/access_token'
oauth = OAuth1Session(consumer_key,
                     client_secret=consumer_secret,
                     resource_owner_key=resource_owner_key,
                     resource_owner_secret=resource_owner_secret,
                     verifier=verifier)
oauth_tokens = oauth.fetch_access_token(access_token_url)

access_token = oauth_tokens['oauth_token']
access_token_secret = oauth_tokens['oauth_token_secret']

# Make the request
oauth = OAuth1Session(consumer_key,
                       client_secret=consumer_secret,
                       resource_owner_key=access_token,
                       resource_owner_secret=access_token_secret)
response = oauth.get("https://api.twitter.com/1.1/search/tweets.json", params = params)
print("Response status: %s" % response.status_code)
print("Body: %s" % response.text)
r = json.loads(response.text)
tweets = r['statuses']
for tweet in tweets:
    print(tweet['text'])
