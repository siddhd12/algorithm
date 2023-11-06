# 제출용
import sys
from collections import deque
num = int(sys.stdin.readline().strip())
card = deque(range(1, num+1))
while len(card) > 1:
    card.popleft() # 맨 앞에 있는 카드를 버림
    card.rotate(-1) # 맨 뒤에 있는 카드를 맨 앞으로 이동
print(card[0])

#########################################################################
# 더러운 Deque  분명히 시간복잡도 N이였는데...이상하다 
# 초기_1
import sys
num= int(sys.stdin.readline().strip())
card=list(range(1,num+1))
for i in range(num):
    print(card)
    if len(card)==1: #하나 남기면 남기기
        break
    card.pop(0) # 1을 버림 
    card.append(card[0])#  맨끝값으로 추가
    card.pop(0)
print(card[0])

# for 문을써서 너무 느린가 싶었다... N^2나옴..
######################################################################################
# 마지막
import sys
num=int(sys.stdin.readline().strip())
card=list(range(1,num+1))
while len(card) >1:
    card.pop(0) #1을 버림 
    card.append(card[0])#  맨끝값으로 추가
    card.pop(0)
print(card[0])    
# while로 돌려서 더 빠르게 해서 복잡도를 낮췄다.. N으로 줄임 근데도 안됨 개억울...
# 그이후에 함수 Deque 를 쓰지않고 하는 방법을 알아냈다 어차피 홀수번은 버리기에 짝수번만 갖고와서
# 계산 하면 더 쭐어들고 홀수번째면 그냥하고 짝수번이면 다시 한번더 계산 하는방식이면 되지않을까 라는 생각
#####################################



#1,2,3,4
# 1을 버림
# 2,3,4
# 뒤짚는게 아니라 맨밑으로
# 3,4,2
# 3을 버림
# 4,2
# 4를 밑으로 
# 2,4
# 2를 버림
# 4 


# 원리
# 1을 버림
# 2,3,4,5,6
# 2를 맽밑으로
# 3,4,5,6,2
# 3을 버려
# 4,5,6,2
# 4를 맨 밑으로 
# 5,6,2,4
# 5를 버려
# 6,2,4
# 6을 맨 밑으로 
# 2,4,6
# 2를 버려
# 4,6
# 4를 맨 밑으로 
# 6,4 
# 6을 버려
# 4
