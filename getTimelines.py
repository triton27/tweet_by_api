import json, config
from requests_oauthlib import Oauth1Session

ck = config.CONSUMER_KEY
cs = config.CONSUMER_SECRET
at = config.ACCESS_TOKEN
ats = config.ACCESS_TOKEN_SECRET

# OAuth で取得する
twitter = Oauth1Session(ck, cs, at, ats)

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

# 取得する tweet 数を10件に設定
params = {'count': 10}
req = twitter.get(url, params = params)

if req.status_code == 200:
    # レスポンスは JSON なので、 parse する
    timeline = json.load(req.text)
    for tweet in timeline:
        print(tweet["text"])

else:
    print("Error: %d" % req.status_code)
