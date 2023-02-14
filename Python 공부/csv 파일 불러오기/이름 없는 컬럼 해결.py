# 첫 번째 컬럼을 index로 사용하도록 지정하여 로드
input = pd.read_csv('data.csv', index_col = 0)


# Unnamed: 0 컬럼을 drop하여 제거
input.drop(['Unnamed: 0'], axis = 1, inplace = True)

# 위/아래로 합치기 - 행 기준
pd.concat([df1, df2], axis = 0)

# 옆으로 합치기 - 열 기준
pd.concat([df1, df2], axis = 1)

