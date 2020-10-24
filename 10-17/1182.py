import sys

count = 0
def calc(sum, i):
    global count
    if N == i:
        return
    if sum + data[i] == S:
        count += 1
    calc(sum+data[i],[i+1])
    calc(sum, i+1)

f = sys.stdin # 코딩데스트 용도
#f = open('data.txt', 'r') #PC용 테스트용도
N, S = map(int, f.readline().split())
data = list(map(int, f.readline().split()))


calc(0,0)
print (count)
