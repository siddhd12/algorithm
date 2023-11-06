result=int(input()) # 영수증 총계산
num= int(input()) # 물건 종류 == 반복횟수
sum=0
for i in range(num): # 물건 종류 만큼 반복 
    a,b=map(int,input().split()) # 가격 * 갯수
    sum=sum+(a*b) # 합계
if result == sum: # 합계랑 영수증 계산이 같을경우
    print("Yes")
else:# 합계랑 영수증이 다를 경우
    print("No")
