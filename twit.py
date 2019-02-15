import tweepy
from tweepy import OAuthHandler

consumer_key = 'X2xwBghwKRIE2SPeLvvH1pZ7f'
consumer_secret = 'zcoFz18rFB2uvs1rUX4pGeibFB2YG6qoP4kl7TBZScleaWP2ul'
access_token = '1094650909576101888-ngJPWa3ojdJsJbS5dabTlU3G9XDBfO'
access_secret = 'gwb8vu1bJG4OUsqx2s6pGbLN5oc9BvKs1N1XSk1j0bIPO'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# for status in tweepy.Cursor(api.home_timeline).items(10):
#     # Process a single status
#     print(status.text)

query = 'python'
#as of time of writing deeplocal has tweeted 4173 times
max_tweets = 4173
searched_tweets = []
last_id = -1
while len(searched_tweets) < max_tweets:
    count = max_tweets - len(searched_tweets)
    try:
        new_tweets = api.search(q=query, count=count, max_id=str(last_id - 1))
        if not new_tweets:
            break
        searched_tweets.extend(new_tweets)
        print(new_tweets.__dict__)
        last_id = new_tweets[-1].id
    except tweepy.TweepError as e:
        break
