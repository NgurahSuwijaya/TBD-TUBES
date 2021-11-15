import tweepy

api_key = "Qi2fzEgqZt4WyllQJiihhHxSG"
api_secret_key = "t5D7hWjoKr8kT7hK8Dr8bMgltDYRvCrcohuh0UYO7TnEZby7VZ"
access_token = "1212381671556673538-JfHgsOG7P72JWRbwb1E6xSt4UEH4Qm"
access_token_secret_key = "11oyOKdxOGg0BdZYAJUpPvfepv5MUYchNzu9GNAZREovS"

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret_key)
api = tweepy.API(auth)

resultSearch = api.search_tweets(q="kenapa bitcoin", lang="id", count="100")

for tweet in resultSearch:
    print(tweet.text)