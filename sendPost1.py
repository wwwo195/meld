import pytumblr
import json

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
    '<consumer_key>',
    '<consumer_secret>',
    '<oauth_token>',
    '<oauth_secret>',
)

with open('blazeacrossthenorth-blog.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())


# Make the request
client.info()


for i in data["posts"]:
    if i["type"] == "regular":
        client.create_text('whitelikeheaven', state="draft", slug=i["slug"], title=i["regular-title"], body=i["regular-body"], date=i["date"])
    elif i["type"] == "audio":
            client.create_audio('whitelikeheaven', state="draft", slug=i["slug"], caption=i["audio-caption"], date=i["date"], tags=i["tags"])
    elif i["type"] == "video":
        try:
            client.create_video('whitelikeheaven', state="draft", caption=i["video-caption"], date=i["date"], tags=i["tags"], embed=i["video-source"])
        except KeyError:
            client.create_video('whitelikeheaven', state="draft", caption=i["video-caption"], date=i["date"], embed=i["video-source"])
    elif i["type"] == "photo":
        client.create_photo('whitelikeheaven', state="draft", slug=i["slug"], format=i["format"], source=i["photo-url-500"], caption=i["photo-caption"], date=i["date"])
        
        
        
