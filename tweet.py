import config
from requests_oauthlib import OAuth1Session

ck = config.CONSUMER_KEY
cs = config.CONSUMER_SECRET
at = config.ACCESS_TOKEN
ats = config.ACCESS_TOKEN_SECRET

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

# OAuth 認証で POST で投稿する
twitter = Oauth1Session(ck, cs, at, ats)
req = twitter.post(url, params = params)

# tweet 本文
params = {"status": "Hello, World!"}

if req.status_code == 200:
    print("OK")
else:
    print("Error: %d" % req.status_code)
