import tweepy
import csv
import pandas as pd


api_key = "Qi2fzEgqZt4WyllQJiihhHxSG"
api_secret_key = "t5D7hWjoKr8kT7hK8Dr8bMgltDYRvCrcohuh0UYO7TnEZby7VZ"
access_token = "1212381671556673538-JfHgsOG7P72JWRbwb1E6xSt4UEH4Qm"
access_token_secret_key = "11oyOKdxOGg0BdZYAJUpPvfepv5MUYchNzu9GNAZREovS"

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret_key)
api = tweepy.API(auth)

keyparam="cryptocurency"
csvfile = open(keyparam+".csv","a+",newline="",encoding="utf-8")
csvWriter = csv.writer(csvfile)
c = []
u = []
t = []


for tweet in tweepy.Cursor(api.search_tweets,q=keyparam, count=1000, lang="id").items():
    print(tweet.created_at,tweet.user.name, tweet.text)
    c.append(tweet.created_at)
    u.append(tweet.user.name)
    t.append(tweet.text.encode("utf-8"))
    tweetss = [tweet.created_at,tweet.user.name,tweet.text.encode("utf-8")]
    csvWriter.writerow(tweetss)

dictTweets = {"waktu":c,"username":u,"text":t}
df = pd.DataFrame(dictTweets,columns=["waktu","username","teks"])
df
