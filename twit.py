import tweepy
from tweepy import Cursor
from tweepy import OAuthHandler
from datetime import datetime
from collections import Counter

# Twitter API keys and secrets
consumer_key = 'X2xwBghwKRIE2SPeLvvH1pZ7f'
consumer_secret = 'zcoFz18rFB2uvs1rUX4pGeibFB2YG6qoP4kl7TBZScleaWP2ul'
access_token = '1094650909576101888-ngJPWa3ojdJsJbS5dabTlU3G9XDBfO'
access_secret = 'gwb8vu1bJG4OUsqx2s6pGbLN5oc9BvKs1N1XSk1j0bIPO'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# Set user for later use and create all needed variables
item = api.get_user("deeplocal")
hashtags = []
tweet_count = 0

# Call API and get tweets, starts from most recent tweets and works backward
for status in Cursor(api.user_timeline, id="deeplocal").items():
    tweet_count += 1

    # Check to see if tweet falls in range (2017) and if so extract the hashtag and store it while checking to see if
    # we have already stored the hashtag from a previous tweet
    if status.created_at > datetime(2017,1,1,0,0) and status.created_at < datetime(2017,12,31,11,59,59):
        if hasattr(status, "entities"):
            entities = status.entities
            if "hashtags" in entities:
                for ent in entities["hashtags"]:
                    if ent is not None:
                        if "text" in ent:
                            hashtag = ent["text"]
                            if hashtag is not None:
                                hashtags.append(hashtag)
    # Since we are working backwards, once we pass 2017 there is no need to go further
    if status.created_at < datetime(2017,1,1,0,0):
        break

# Print out the resulting list using Counter
print("Hashtag frequency 2017:")
for item, count in Counter(hashtags).most_common():
    print(item + "\t" + str(count))

# Print out some fun facts
print("All done. Processed " + str(tweet_count) + " tweets.")
print(str(len(hashtags)) + " Hashtags used in total from 2017. " + str(len(Counter(hashtags).keys())) + " unique.")