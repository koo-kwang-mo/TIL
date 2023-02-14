# 소상공인 수 예측하기.

링크 : https://www.kaggle.com/competitions/godaddy-microbusiness-density-forecasting/data


## 데이터 설명

기차.csv

row_id- 행의 ID 코드입니다.
cfips- Federal Information Processing System을 사용하는 각 카운티의 고유 식별자입니다. 처음 두 자리는 주 FIPS 코드에 해당하고 다음 3자리는 카운티를 나타냅니다.
county_name- 카운티의 서면 이름.
state_name- 주의 이름.
first_day_of_month- 매월 1일의 날짜입니다.
microbusiness_density- 해당 카운티의 18세 이상 인구 100명당 소상공인. 대상 변수입니다. 밀도를 계산하는 데 사용되는 인구 수치는 매년 기본 인구 데이터를 제공하는 미국 인구 조사국에서 제공하는 업데이트 속도로 인해 2년 지연됩니다. 2021년 밀도 수치는 2019년 인구 수치 등을 사용하여 계산합니다.
active- 카운티의 소상공인 수. 테스트 세트에는 제공되지 않습니다.
sample_submission.csv 유효한 샘플 제출입니다. 이 파일은 대회 내내 변경되지 않습니다.

row_id- 행의 ID 코드입니다.
microbusiness_density- 대상 변수.
test.csv 제출 행의 메타데이터입니다. 이 파일은 대회 내내 변경되지 않습니다.

row_id- 행의 ID 코드입니다.
cfips- Federal Information Processing System을 사용하는 각 카운티의 고유 식별자입니다. 처음 두 자리는 주 FIPS 코드에 해당하고 다음 3자리는 카운티를 나타냅니다.
first_day_of_month- 매월 1일의 날짜입니다.
섬겨 진_테스트.csv 제출 기간 동안에는 가장 최근 달의 데이터만 공개 순위표에 사용됩니다 . 그보다 오래된 모든 테스트 세트 데이터는 공개 _테스트.csv 에 게시되며 소기업 보고서의 일반적인 데이터 릴리스 주기를 따릅니다. 우리는 2월 중순 에 Reliable_test.csv 사본 1개를 게시할 예정입니다. 이 파일의 스키마는 train.csv 와 일치합니다 .

census_starter.csv data.census.gov 에 있는 Census Bureau의 American Community Survey(ACS)에 있는 유용한 열의 예입니다 . 백분율 필드는 ACS에서 제공한 원시 개수에서 파생되었습니다. 모든 필드는 주어진 소기업 데이터 업데이트가 게시된 시점에 사용 가능한 정보와 일치하기 위해 2년의 시차가 있습니다.

pct_bb_[year]- 모든 유형의 광대역에 액세스할 수 있는 카운티의 가구 비율. ACS 표 B28002에서 파생됨: 가구 내 인터넷 구독의 존재 및 유형.
cfips- CFIPS 코드.
pct_college_[year]- 4년제 대학 학위를 가진 25세 이상의 카운티 인구 비율. ACS 표 S1501에서 파생됨: 교육 성취도.
pct_foreign_born_[year]- 미국 밖에서 태어난 카운티 인구의 비율. ACS 테이블 DP02에서 파생됨: 미국에서 선택된 사회적 특성.
pct_it_workers_[year]- 카운티에서 정보 관련 산업에 고용된 인력의 비율. ACS 표 S2405에서 파생됨: 16년 이상 민간 고용 인구를 위한 직업별 산업.
median_hh_inc_[year]- 카운티의 중간 가계 소득. ACS 표 S1901에서 파생됨: 지난 12개월 동안의 소득(2021년 인플레이션 조정 달러).


## 진행상황

1) 2.8 시작
   1) 데이터를 살펴보고 이해하기
      1) cfips가 주워지고 대부분의 데이터가 rowid를 통해 합쳐질만 하겠다. => federal information processiong  system에서 추가적인 데이터를 얻을 수 있다면 활용도도 높고 용이할 것이다.
      2) 