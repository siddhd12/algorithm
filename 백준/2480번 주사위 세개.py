문제 해석하면서 풀이용
x,y,z  = map(int, input().split()) #주사위 3개 던짐 
dize_one=[x,y,z] # 주사위 값 넣음

print(f"x의 값:{x}/ y의 값:{y} /  z의 값:{z}",)
print(dize_one)
dize=list(set(dize_one))  # 3개 가 같으면 길이는 1개  나옴
                # 2개가 같으면 길이는 2개 나옴 
                # 다 다르면 길이는 3개 나옴
print(type(dize))
print(max(dize))
print("길이는",len(set(dize)))
if len(set(dize))==1: # 3개 조건
    result=10000+(x*1000)
    print("3개가 같음",result)
elif len(set(dize))==2: # 2개 조건
    for element in dize:  # 중복을 제거한 리스트 안에 원소를 뽑음
        if dize_one.count(element)>1: # 중복이 있는 리스트의 원소값이 1개 이상이면 중복된 값 
            result= 1000+(element*100) # 같은 값 계산 
    
    print("2개가 같음",result)
else:# 완료
    result=max(dize)
    result=result*100
    print("다 다름",result)

# 조건 3개 
#같은 값 3개 나오는 조건 ->  10,000원+(같은 눈)×1,000
# 같은 값 2개 나오는 조건 -> 1,000원+(같은 눈)×100
# 다 다른 값 나오는 조건 -> (그 중 가장 큰 눈)×100원



#제출용

x,y,z  = map(int, input().split()) #주사위 3개 던짐 
dize_one=[x,y,z] # 주사위 값 넣음
dize=list(set(dize_one))  # 3개 가 같으면 길이는 1개  나옴
                # 2개가 같으면 길이는 2개 나옴 
                # 다 다르면 길이는 3개 나옴
if len(set(dize))==1: # 3개 조건
    result=10000+(x*1000)
elif len(set(dize))==2: # 2개 조건
    for element in dize:  # 중복을 제거한 리스트 안에 원소를 뽑음
        if dize_one.count(element)>1: # 중복이 있는 리스트의 원소값이 1개 이상이면 중복된 값 
            result= 1000+(element*100) # 같은 값 계산 
else:# 완료
    result=max(dize)
    result=result*100
print(result)
