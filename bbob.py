import tweepy
import json
from random import randint

class composeMessage:
    def ph1(self, dictionary):
        word1 = dictionary[randint(0, len(dictionary) - 1)]
        word2 = dictionary[randint(0, len(dictionary) - 1)]
        while word1 == word2:
            word2 = dictionary[randint(0, len(dictionary) - 1)]
        return 'You are ' + word1[2] + ' ' + word1[0] + ' ' + word2[1] + '.'

composeMessage = composeMessage()

tw_apiinfo = json.load(open('api_info.json'))
dictionary = json.load(open('dictionary.json'))['words_l1']

auth = tweepy.OAuthHandler(tw_apiinfo['ckey'], tw_apiinfo['csec'])
auth.set_access_token(tw_apiinfo['atkey'], tw_apiinfo['atsec'])

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True, compression = True)

api.update_status('THIS IS A TEST MESSAGE: ' + composeMessage.ph1(dictionary))