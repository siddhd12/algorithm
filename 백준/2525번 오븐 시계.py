# 제출용 
hour, minute = map(int, input().split()) # 현재 시간 값을 받아옴
oven =int(input()) # 원하는 시간 받아옴
whole_time=(hour*60)+minute+oven  # 전체시간= 현재시간 *60 +현재분 +원하는 분
div_hour= whole_time//60   # 전체시간에서 시간 빼기
if div_hour >= 24: # 24시간 지나면 0으로 초기화 시키기
    div_hour=div_hour-24
div_minute= whole_time%60   # 전체시간에서 분만 빼기 
print(div_hour,div_minute)

#########################################################################################
# 천천히 풀면서 print 하면서 함

hour, minute = map(int, input().split()) # 현재 시간 값을 받아옴
oven =int(input()) # 원하는 시간 받아옴
whole_time=(hour*60)+minute+oven  # 전체시간= 현재시간 *60 +현재분 +원하는 분
print(whole_time)
div_hour= whole_time//60   # 전체시간에서 시간 빼기
if div_hour >= 24:
    div_hour=div_hour-24
div_minute= whole_time%60   # 전체시간에서 분만 빼기 
print(f"원하는 시간은{hour}시{minute}분에서{oven} 더하기")
print("div hour", div_hour,"div minute", div_minute) #  결과
#########################################################################################3
