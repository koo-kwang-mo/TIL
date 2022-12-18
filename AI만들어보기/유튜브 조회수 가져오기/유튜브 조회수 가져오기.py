import pandas as pd
import numpy as numpy
import seaborn as sns
import matplotlib.pyplot as plt
import os

KRvideo = pd.read_csv("KR_youtube_trending_data.csv")#csv 파일 로드
#KRvideo = pd.read_csv("KR_youtube_trending_data.csv", engine="python", error_bad_lines="false")#에러 없애기

# 데이터 프레임 형태 파악 (상위 5개 행 x 전체 열 출력)
#KRvideo.head()

#영상제목(title), 채널명(channelTitle), 조회수(view_count)만 사용할 예정

# 데이터 프레임의 전체 정보 요약
#KRvideo.info()

df = KRvideo[["title", "channelTitle", "view_count"]]#데이터 다듬기

#지금은 조회수 순이 아닌 가장 처음의 데이터 셋에 저장된 순서이므로 내림차순(큰 것이 위에 오도록)으로 정렬
df_sorted = df.sort_values(by='view_count', ascending=False)

# 영상제목과 채널명이 둘 다 중복인 영상 제거
df_sorted_latest = df_sorted.drop_duplicates(['title','channelTitle'], keep='first')

# 상위 10개 영상 확인
#df_sorted_latest.head()


#채널별 조회수 합계 및 조회수 상위 20개 채널 확인

# groupby() : 특정 컬럼을 기준으로 그룹을 묶어서 평균, 합계를 낼 수 있음

# 채널별 조회수 합계 계산
df_channel_view_sum = df_sorted_latest.groupby(['channelTitle']).sum()

# 채널별 조회수 내림차순 정렬
df_channel_view = df_channel_view_sum.sort_values(by='view_count', ascending=False)

# 총 2253개의 채널 중 상위 20개 채널만 가져오기
df_channel_view_top20 = df_channel_view[:20]

# 데이터 출력
#df_channel_view_top20


#그래프로 데이터 시각화
#시각화를 위해서 데이터에 index를 추가해줄 필요가 있습니다. 0~99까지의 index가 있어야지 그래프가 그려진답니다.
df_channel_view_top20_index = df_channel_view_top20.reset_index()

# 그래프 출력 시 이상한 에러들 무시
import warnings
warnings.filterwarnings("ignore")


# 그래프 그릴 때 한글 깨짐 방지 설정
import os

# Mac OS의 경우와 그 외 OS의 경우로 나누어 설정

if os.name == 'posix':
    plt.rc("font", family="AppleGothic")

else:
    plt.rc("font", family="Malgun Gothic")


# 그래프 사이즈 설정
plt.figure(figsize=(10,10))


# seaborn 패키지로 수평막대 그래프 그리기
sns.barplot(x='view_count', y='channelTitle', data=df_channel_view_top20_index)

plt.show()