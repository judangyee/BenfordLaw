from benfordslaw import benfordslaw
import FinanceDataReader as fdr

dataset = fdr.DataReader("BTC/KRW", "1980")
df = dataset['Close']
# 초기화하기
bl = benfordslaw( )

# 데이터 셋 입력하기
results = bl.fit(df)    # dataset 은 pandas 의 Series 형태로 입력

# 검사결과 보기(그래프로)
bl.plot() 
