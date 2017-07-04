import json
import requests
 
request_url = 'http://api.tumblr.com/v2/blog/blazeacrossthenorth-blog.tumblr.com/posts/text?api_key=sLL9UAvrXyfsCxqB3njlF988Lkcf13HP7mQkZjebiphXgcauJR'
all_post = []
offset = 0
posts_still_left = True
while posts_still_left:
    request_url += "&offset=" + str(offset)
    tumblr_response = requests.get(request_url).json()
    total_posts = tumblr_response['response']['total_posts']
    for post in tumblr_response['response']['posts']:
        p = TumblrPost(post['post_url'], post['date'], post['body'], '', post['title'])
        all_posts.append(p)
        offset += 20
    if offset > total_posts:
        posts_still_left = False
