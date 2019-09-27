import tweepy
import json
from random import randint
from time import sleep

class composeMessage:
    def ph1(self, w1dic, w2dic):
        w1_lst = w1dic[randint(0, len(w1dic) - 1)]
        w2_lst = w2dic[randint(0, len(w2dic) - 1)]
        try:
            temp = w1_lst[2]
            temp = w2_lst[1]
            while w1_lst[1] == w2_lst[1]:
                print(w2_lst[0])
                w2_lst = w2dic[randint(0, len(w2dic) - 1)]
        except IndexError:
            pass
        word1 = w1_lst[0]
        word2 = w2_lst[0]
        if len(w1_lst) == 3:
            atcl = w1_lst[2]
        else:
            atcl = w1_lst[1]
        return 'You are ' + atcl + ' ' + word1 + ' ' + word2 + '.'
composeMessage = composeMessage()

def sleeptimer(secs):
    i = 0
    while i < secs:
        sleep(1)
        print(str(secs - i) + ' seconds remaining...')

user = True

tw_apiinfo = json.load(open('api_info.json'))

auth = tweepy.OAuthHandler(tw_apiinfo['ckey'], tw_apiinfo['csec'])
auth.set_access_token(tw_apiinfo['atkey'], tw_apiinfo['atsec'])

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True, compression = True)


while True:
    dictionary = json.load(open('dictionary.json'))
    users = json.load(open('accounts.json'))['account_list']
    w1dic = []
    w2dic = []
    for item in dictionary['words_l1']:
        w1dic.append([item[0], dictionary['words_l1'].index(item),item[2]])
        w2dic.append([item[1], dictionary['words_l1'].index(item)])
    for item in dictionary['words_l1_adj']:
        w1dic.append([item[0], item[1]])
    for item in dictionary['words_l1_noun']:
        w2dic.append([item])
    if user:
        message = 'THIS IS A TEST MESSAGE: @' + users[randint(0, len(users) - 1)] + ' ' + composeMessage.ph1(w1dic, w2dic)
    else:
        message = 'THIS IS A TEST MESSAGE: ' + composeMessage.ph1(w1dic, w2dic)
    try:
        api.update_status(message)
        print('Sent message "' + message + '"')
    except:
        print('Failed to update status')
        break
    sleeptimer(24 * 60 * 60) # 24hrs * 60mins * 60secs