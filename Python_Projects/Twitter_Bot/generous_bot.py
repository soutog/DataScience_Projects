import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

#Generous Bot - Follows people back
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
      if follower.name == 'Usernamehere':
        print(follower.name)
        follower.follow()
