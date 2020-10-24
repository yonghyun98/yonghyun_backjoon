import sys

#f = sys.stdin # 코딩데스트 용도
f = open('data.txt', 'r') #PC용 테스트용도
N, S = map(int, f.readline().split())
data = list(map(int, f.readline().split()))
count = 0

stack =[] # 처리할 작업
stack.append(0,0) # sum, i
while stack: # 작업을 모두 처리할 때 까지
    sum, i = stack.pop() # 작업 시작
    if i == N: # data 변수를 모두 확인함
        continue # 더이상 조회할 data가 없음

    if sum + data[i] == S: # 합이 S가 되었으면
        count += 1 # 카운팅

    stack.append((sum+data[i], i+1)) # 다음에 확인할 작업
    stack.append((sum, i+1)) 

print (count)