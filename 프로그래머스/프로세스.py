#제출용
import queue
def solution(priorities, location):
    cnt=1
    max_num=max(priorities) # 우선순위 max
    que = queue.Queue()  # que 생성 (대기열)
    for x in range(len(priorities)):
        que.put((priorities[x],x))  # 우선순위, index

    while max_num>=0:
        item = que.get() # 요소를 뽑아냄 
        if item[0]==max_num:#  여기서 판별  
            if item[1]==location:
                break
            cnt+=1
            priorities.remove(max_num)
            try:
                max_num=max(priorities)
            except:
                break
        elif item[0]<max_num: # max 보다 작으면 뒤로 값보내기
            que.put(item)
    return cnt
  #####################################################################################
  # 초기엔 우선순위 큐로 가능할 줄 알았다.
  rom queue import PriorityQueue
que = PriorityQueue(maxsize=9) # 9까지 우선 순위를 정함
for i in range(len(pro)):
    que.put((len(pro)-pro[i],a[i])) # 우선 순위 정하기 
while not que.empty():
    print(que.get()[1])
# for i in range(len(pro)):
#     b=que.get()[1]
#     print(a)
#     step+=1
#     print("뽑는거",b)
#     print("스탭",step)
#     if b==a[loc]:
#         print(step)
#     우선순위가 같은 경우에서 c뒤에꺼 뽑아야하는데 못뽑겠닫 꾀꼬리
#################################################################################################
# 우선순위 큐를 포기 다시 짰다...
import queue

priorities=[1,1,9,1,1,1]  # 우선 순위
location=0 #위치 찾기 
cnt=1
max_num=max(priorities) # 우선순위 max
que = queue.Queue()  # que 생성 (대기열)
for x in range(len(priorities)):
    que.put((priorities[x],x))  # 우선순위, index
print("크기는",que.qsize())
# for y in range(que.qsize())

while max_num>=0:
    print("스탭",cnt)
    item = que.get() # 요소를 뽑아냄 
    if item[0]==max_num:#  여기서 판별 
        print("뽑아낸다",max_num,item[0],item[1],"스탭은",cnt) 
        if item[1]==location:
            print("찾았다...",item[0],item[1],cnt)
        cnt+=1
        priorities.remove(max_num)
        try:
            max_num=max(priorities)
        except:
            break
    elif item[0]<max_num: # max 보다 작으면 뒤로 값보내기
        print("뒤로보냄",que.put(item))

        
#     print("max보다 큼 ",max,que.get()[0])
#     max-=1


# 3,2,2,1
# 어떻게 값 중에서 max를 알아봄 max() 함수 이용
# 반복문에서
# 1단계 item[0]이 ==max 면 뽑는다
# 2단계 item[0]이 max보다 작으면 값을 뒤로 붙인다
# 3단계 max와 같은 값이 없으면 낮춘다
