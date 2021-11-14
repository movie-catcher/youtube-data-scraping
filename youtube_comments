import pandas
from googleapiclient.discovery import build
df = pandas.read_excel('results_극한직업1.xlsx', header = 1)
api_key="AIzaSyDjNOEzDgg3NzfGkwu6iUAs-oImZffOyyQ"
video_id = '8iQg4napg90'
##video_id_list=['YcMZZ3sjfxk','7DRDMuMdxVY','8iQg4napg90']
comments = list()

api_obj = build('youtube', 'v3', developerKey=api_key)
response = api_obj.commentThreads().list(part='snippet, replies', videoId=video_id, maxResults=1000).execute()

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
video_list_num=[video_id]
df2 = pandas.DataFrame(data=comments, columns=['comment', 'author', 'date', 'num_likes'])
df2['videoId']=video_id
df3=pandas.concat([df,df2], axis = 0)
df2.to_excel('results_극한직업1.xlsx', index=None)
