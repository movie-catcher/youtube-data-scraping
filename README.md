#### 유튜브 데이터 스크래핑
- [📺  유튜브 영상 데이터 수집](#--유튜브-영상-데이터-수집)
- [💬  유튜브 영상 컨텐츠 댓글 데이터 수집](#--유튜브-영상-컨텐츠-댓글-데이터-수집)
- [🤖 감성 분석](#-감성-분석)


* * * 

## ⚒ Stacks
![Python](https://img.shields.io/badge/-Python-306998?logo=python&logoColor=ffd43b&style=for-the-badge)
![Jupyter Notebook](https://img.shields.io/badge/-jupyter%20notebook-727272?logo=jupyter&logoColor=eb7633&style=for-the-badge)
![selenium](https://img.shields.io/badge/-selenium-08ad19?logo=jupyter&logoColor=ffffff&style=for-the-badge)
![beautifulsoup](https://img.shields.io/badge/-beautifulsoup4-000?logo=bs4&logoColor=ffffff&style=for-the-badge)
![requests](https://img.shields.io/badge/-requests-000?logo=requests&logoColor=ffffff&style=for-the-badge)

![numpy](https://img.shields.io/badge/-numpy-ffd43b?logo=numpy&logoColor=306998&style=for-the-badge)
![pandas](https://img.shields.io/badge/-pandas-150454?logo=pandas&logoColor=ffffff&style=for-the-badge)

<br/>

# 📺  유튜브 영상 데이터 수집 
* 영화와 관련된 유튜브 영상 컨텐츠 정보를 수집
* Youtueb Data API v3를 사용
* 영화의 제목을 키워드로 검색할 경우 영화와 상관없는 영상이 포함되는 경우가 많음 -> 키워드 선정
* **검색 키워드**
  * 영화
  * 명장면
  * 리뷰
  * 해석
  * 의미

|file|desc|
|:---:|---|
|[소스코드](./src/get_youtube_video.ipynb)|1. `영화 제목 + 키워드`를 검색하여 데이터 수집(한 영화의 키워드 당 20개의 영상) <br/>2. 최대 100개의 영상을 조회수 순으로 정렬 <br/>3. 상위 10개의 영상 추출|
|[data](./data/movieVideoList/filtered)|영화 당 10개의 영상 리스트 정보 데이터|

<br/>

# 💬  유튜브 영상 컨텐츠 댓글 데이터 수집
* 1에서 수집한 영상 데이터를 통한 해당 영상의 모든 댓글 데이터 수집
* Youtueb Data API v3를 사용

|file|desc|
|:---:|---|
|[소스코드](./src/get_youtube_comments.py)|해당 영상의 모든 댓글 데이터 수집|
|[data](./data/youtube_comments)|해당 영상의 모든 댓글 데이터|


# 🤖 감성 분석
* 유튜브 영상 컨텐츠 댓글을 감성 분석 시행
* [-10, 10] 범위로 -10에 가까울 수록 부정, 10에 가까울 수록 긍정
* 베이스 모델 : Aurora3

|file|desc|
|:---:|---|
|[소스코드](./src/sentiment_analysis_2.ipynb.py)|유튜브 댓글의 감성 분석|
|[data](./data/comments_sentiment_analysis)|모든 댓글 데이터의 감성 분석 결과|
