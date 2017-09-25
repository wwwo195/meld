import pytumblr
import json

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
  'sLL9UAvrXyfsCxqB3njlF988Lkcf13HP7mQkZjebiphXgcauJR',
  '8DLTm4aTkzjk5rnFovEVM0fsxkglgSdKKQ01iw6EkdDaJzgMsc',
  'JqZxy3ElqYXutiZKW05kuXbiMa9XPz0K345aNF2fEAfd4rVIYb',
  'Va3a3UR1edTKnrUMk6x2PQanr0SBPwmV7p7H5bXmyXxnWLJHDH'
)

with open('blazeacrossthenorth-blog.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())


# Make the request
client.info()


for i in data["posts"]:
    if i["type"] == "regular":
        client.create_text('whitelikeheaven', state="draft", slug=i["slug"], title=i["regular-title"], body=i["regular-body"], date=i["date"])
    elif i["type"] == "audio":
        client.create_audio('whitelikeheaven', state="draft", slug=i["slug"], title=i["regular-title"], caption=i["audio-caption"], date=i["date"])
    elif i["type"] == "video";
        client.client_video('whitelikeheaven', state"draft", title=i["regular-title"], caption=i["video-caption"], date=i["date"])
        
        
