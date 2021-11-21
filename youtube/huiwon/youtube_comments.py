import pandas
from googleapiclient.discovery import build
# 영화별 video Id 가 있는 파일 가져오기
datacsv=pandas.read_csv('movieVideoList_0_19 (1).csv')
# 특정 영화의 vieod Id를 리스트로 저장
video_id_list=list(datacsv.loc[datacsv['영화 제목'] == '분노의 질주: 홉스&쇼','영상 id'])

for i in range(len(video_id_list)):
    video_id = video_id_list[i]
    
    # 미리 만들어 놓은 dataframe 불러오기
    df = pandas.read_excel('youtube_comments_분노의 질주 홉스&쇼.xlsx', usecols = ['comment', 'author', 'date', 'num_likes', 'videoId'])
    # 유튜브 api key
    api_key="AIzaSyBXR-xCJ4A8JJscWCqozjUuMnpYuFg9PBk"
    comments = list()

    api_obj = build('youtube', 'v3', developerKey=api_key)
    response = api_obj.commentThreads().list(part='snippet, replies', videoId=video_id, maxResults=100).execute()

    while response:
        
        #페이지를 넘겨가며 끝까지 추출
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']

            #유튜브 api에서 댓글, 작성자, 작성시간(작성 날짜만), 좋아요 개수 추출
            comments.append([comment['textDisplay'], comment['authorDisplayName'], comment['publishedAt'][0:10], comment['likeCount']])
 
            if item['snippet']['totalReplyCount'] > 0:

                #대댓글 추출
                for reply_item in item['replies']['comments']:
                    reply = reply_item['snippet']
                    comments.append([reply['textDisplay'], reply['authorDisplayName'], reply['publishedAt'][0:10], reply['likeCount']])
 
        if 'nextPageToken' in response:
            response = api_obj.commentThreads().list(part='snippet,replies', videoId=video_id, pageToken=response['nextPageToken'], maxResults=100).execute()
        else:
            break
    df2 = pandas.DataFrame(data=comments, columns=['comment', 'author', 'date', 'num_likes'])

    #video Id로 댓글의 출처 구분
    df2['videoId']=video_id
    df3=pandas.concat([df,df2], axis = 0)
    df3.to_excel('youtube_comments_분노의 질주 홉스&쇼.xlsx', index=None)

#댓글을 모두 추출한 데이터에서 개봉일 이후 1달까지의 댓글만 남기고 삭제
df4=pandas.read_excel('youtube_comments_분노의 질주 홉스&쇼.xlsx', usecols = ['comment', 'author', 'date', 'num_likes', 'videoId'])
idx_date = df4[df4['date'] > '2019-09-14'].index
df5=df4.drop(idx_date)
df5.to_excel('youtube_comments_분노의 질주 홉스&쇼.xlsx', index=None)
