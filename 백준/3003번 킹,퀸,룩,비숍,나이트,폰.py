chase=[ 1,1,2,2,2,8]
insert = map(int,input().split())
for index,value in enumerate(insert):
    print(chase[index]-value, end=" ")