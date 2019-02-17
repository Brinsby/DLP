import tweepy
from tweepy import Cursor
from tweepy import OAuthHandler
from datetime import datetime
from collections import Counter


consumer_key = 'X2xwBghwKRIE2SPeLvvH1pZ7f'
consumer_secret = 'zcoFz18rFB2uvs1rUX4pGeibFB2YG6qoP4kl7TBZScleaWP2ul'
access_token = '1094650909576101888-ngJPWa3ojdJsJbS5dabTlU3G9XDBfO'
access_secret = 'gwb8vu1bJG4OUsqx2s6pGbLN5oc9BvKs1N1XSk1j0bIPO'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

item = api.get_user("deeplocal")
hashtags = []
tweet_count = 0

for status in Cursor(api.user_timeline, id="deeplocal").items():
    tweet_count += 1

    if status.created_at > datetime(2017,1,1,0,0) and status.created_at < datetime(2017,12,31,11,59,59):
        print(status.created_at)
        if hasattr(status, "entities"):
            entities = status.entities
            if "hashtags" in entities:
                for ent in entities["hashtags"]:
                    if ent is not None:
                        if "text" in ent:
                            hashtag = ent["text"]
                            if hashtag is not None:
                                hashtags.append(hashtag)

    if status.created_at < datetime(2017,1,1,0,0):
        break

print("Most used hashtags:")
for item, count in Counter(hashtags).most_common(10):
    print(item + "\t" + str(count))

print("All done. Processed " + str(tweet_count) + " tweets.")