import pandas as pd

# 간단한 데이터 생성
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# 데이터 프레임 생성
df = pd.DataFrame(data)

# 데이터 프레임 출력
print(df)
