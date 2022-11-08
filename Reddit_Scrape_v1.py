import praw
import sys
try:
    with open ('Reddit-api') as f:
        for num, line in enumerate(f):
            if num == 0:
                cid = line
            if num == 1:
                sec = line 
except: 
    print('Add API client id and user id')



red_account = praw.Reddit (client_id = f'{cid}',
                           client_secret = f'{sec}',
                           user_agent ='Superb-Twist-3912')


usub = input('What sub are you interested in?: ')


sub = red_account.subreddit(f'{usub}')

for post in sub.top(limit=5):
    print(post.title , post.url)
    print()
   