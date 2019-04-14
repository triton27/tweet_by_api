import json, config
from requests_oauthlib import Oauth1Session

ck = config.CONSUMER_KEY
cs = config.CONSUMER_SECRET
at = config.ACCESS_TOKEN
ats = config.ACCESS_TOKEN_SECRET

# OAuth で取得する
twitter = Oauth1Session(ck, cs, at, ats)

url_media = "https://upload.twitter.com/1.1/media/upload.json"
url_text = "https://api.twitter.com/1.1/statuses/update.json"

print("添付画像の名前を入力して下さい(jpg形式のみ)")
media_name = input('>> ')
print('------------------------------------------------------------')

files = {"media": open(media_name + ".jpg", 'rb')}
req_media = twitter.post(url_media, files = files)
req_text = twitter.post(url_text, params = params)

if req_media.status_code != 200:
    print("MEDIA UPLOAD FAILED... %s", req_media.text)
    exit()

media_id = json.loads(req_media.text)['media_id']
print("MEDIA ID: %d" % media_id)

print("何をつぶやきますか？")
tweet = input('>> ')
print('------------------------------------------------------------')

params = {"status": tweet, "media_ids": [media_id]}
req_media = twitter.post(url_text, params = params)

if req_media.status_code != 200:
    print("TEXT UPLOAD FAILED... %s", req_text.text)
    exit()

print("OK")
