import tweepy
import json

tw_apiinfo = json.load(open('api_info.json'))

auth = tweepy.OAuthHandler(tw_apiinfo['ckey'], tw_apiinfo['csec'])
auth.set_access_token(tw_apiinfo['atkey'], tw_apiinfo['atsec'])

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True, compression = True)

api.update_status('Test 2 stupidfaces')