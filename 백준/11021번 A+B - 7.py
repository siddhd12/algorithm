import sys
num=int(sys.stdin.readline().rstrip()) # 반복횟수 넣기 
for i in range(1,num+1): # 반복만큼 계산
    a,b=map(int,sys.stdin.readline().split())# 값넣음
    print(f"Case #{i}: {a+b}")
    # 세번 틀렸는데 case에서 c가 대문자였다..지문을 잘 읽도록 하자
