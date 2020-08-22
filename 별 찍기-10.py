N = int(input()) #N은 3의 거듭 제곱만 input으로 받는다(3, 9, 27, ...)

star = [] 
for _ in range(N):
    star.append(["*" for _ in range(N)])#별을 N개만큼 N번 star 리스트에 넣는다 예) 3일시 ['*','*','*'],['*','*','*'],['*','*','*']

divide = N
cnt = 0
while divide != 1:
    divide /= 3 #3의 거듭 제곱임으로 3으로 나누어 지지 않을 때까지 즉 1이 될 때까지 cnt를 센다
    cnt += 1 # 빈칸이될 인덱스 값으로 사용될 cnt

for n in range(cnt):
    # 빈칸인 인덱스 구하기
    idx = [i for i in range(N) if (i // 3 ** n) % 3 == 1] 
    #i를 3으로 나눈 몫에 n제곱을 하고 그 값에다가 다시 3을 나누어 주어 그 나머지 값이 1이면 빈칸으로 바뀌어야 할 
		#인덱스 값이 된다.		
		for i in idx: 
        for j in idx:
            star[i][j] = " " #인덱스 값을 각각 i, j에 idx 만큼 할당 받아 별을 빈칸으로 바꾸어준다.

# 프린트
for _ in star:
    print("".join(_))