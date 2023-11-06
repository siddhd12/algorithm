import sys
num=int(sys.stdin.readline().rstrip()) # 반복횟수 넣기 
for i in range(num): # 반복만큼 계산
    a,b=map(int,sys.stdin.readline().split())# 값넣음
    print(a+b)
# sys.stdin.readline()은 콘솔에서 입력을 받는 함수
# jupyter notebook에서는 콘솔 입력이 지원되지 않으므로 이 코드를 실행하면 입력을 
# 받을 수 없어서 무한히 대기
# input() 함수는 콘솔에서 사용자로부터 입력을 받는 대화형 함수
# jupyter에서 계속안되서 힘들어서 그냥 코드를 백준에 넣으니까 되었다 계속 삽질함ㅜ
