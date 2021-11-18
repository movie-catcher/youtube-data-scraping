import pandas
from googleapiclient.discovery import build
from pandas.core.frame import DataFrame
import re
data=pandas.DataFrame(index=range(0,95), columns=['영화명', '총 댓글수'])
moviedata=pandas.read_excel("movie_20192020.xlsx")
data['영화명']=moviedata['영화명']

for i in range(80,94):
    movie_name=data.iloc[i,0]
    re_movie_name = re.sub(":","",str(movie_name))
    file_name="youtube_comments_"+re_movie_name+".xlsx"
    commentsdata=pandas.read_excel(file_name)
    comments_count=len(commentsdata)
    data['총 댓글수'][i]=comments_count

data.to_excel('movie_comments_count2.xlsx', index=None)