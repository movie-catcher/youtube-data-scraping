# 댓글 가져오기!

import pandas
from googleapiclient.discovery import build

api_key = 'AIzaSyBoNWXv3_lyCRe05-RoRiF5C3tMmUjH9go'
video_id = 'b_xuj8RzlXQ'

# api_key 가릴까용..?

comments = list()
api_obj = build('youtube', 'v3', developerKey=api_key)
response = api_obj.commentThreads().list(part='snippet,replies', videoId=video_id, maxResults=3000).execute()
 
while response:
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        comments.append([comment['textDisplay'], comment['authorDisplayName'], comment['publishedAt'], comment['likeCount']])
 
        if item['snippet']['totalReplyCount'] > 0:
            for reply_item in item['replies']['comments']:
                reply = reply_item['snippet']
                comments.append([reply['textDisplay'], reply['authorDisplayName'], reply['publishedAt'], reply['likeCount']])
 
    if 'nextPageToken' in response:
        response = api_obj.commentThreads().list(part='snippet,replies', videoId=video_id, pageToken=response['nextPageToken'], maxResults=100).execute()
    else:
        break
df = pandas.DataFrame(comments)
df.to_excel('results_어스.xlsx', header=['comment', 'author', 'date', 'num_likes'], index=None)
