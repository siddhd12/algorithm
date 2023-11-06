# 제출용
def solution(board, moves):
    result=[] #결과 넣을 거 
    num=0  # 중복 갯수 확인 
    for step in moves: # step의 세포 x를 뽑아서 두번째 인덱스 뽑음 
        step-=1 # 1을 뽑을경우 0번째를 뽑기에 -1을해줌
        for i in range(len(board)): # 길이로 첫번째 인덱스 뽑기 
            if board[i][step]==0:
                continue
            else:
                result.append(board[i][step])
                board[i][step]=0
                break
        if len(result)>=2: # result 두개일떄부터 검사 시작한다 두개만 검사해야하니까 
            if result[-2]==result[-1]:  # 첫번째 == 두번째가 같으면  pop
                result.pop(-1)
                result.pop(-1)
                num+=2
    return num
############################################################################
초기
result=[] #결과 넣을 거 
for step in moves: # step의 세포 x를 뽑아서 두번째 인덱스 뽑음 
    step-=1 # 1을 뽑을경우 0번째를 뽑기에 -1을해줌
    print("스탭",step)
    for i in range(len(board)): # 길이로 첫번째 인덱스 뽑기 
        if board[i][step]==0:
            print(board[i][step])
            print("0일때",i,step)
            continue
        else:
            print(i,step)
            print("추가",board[i][step])
            result.append(board[i][step])
            b[i][step]=0
            break
num=0  # 중복 갯수 확인 
y=0   # 위치확인 하기
while y<len(result)-1: # 인덱스 길이 맞추기
    if result[y] == result[y+1]:
        result.remove(result[y]) # remove하면 인덱스가 쭐어듬 
        result.remove(result[y]) # remove하면 인덱스가 쭐어듬 
        num+=2
        print(y,num)
        y=0 # 맞으면 다시 0부터 시작해서 인덱스 조사함 
    else:
        y+=1 # 아닐경우 위에 단계를 찾기위해 +1을함 
# 전체를 다구하고 하는 법으로 정함 테스트 처음은 통과했지만 제출하고 나서 1,2,3,5 만맞고
# 다 틀렸어서 추가하면서 바로 빼야 하나 싶었다...아직도 왜틀린지 모르겠다
#########################################################################################
