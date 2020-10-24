import sys
import queue

#f = sys.stdin
f = open('2606.txt', 'r')

cpt_cnt = int(f.readline())
line_count = int(f.readline())

lines = []
visit =[]

for i in range(cpt_cnt+1):
    lines.append([])
    visit.append(0)

for i in range(line_count):
    src, dst = list(map(int, f.readline().split()))
    lines[src].append(dst)
    lines[dst].append(src)

q = queue.Queue()
q.put(1)

while not q.empty():
    src = q.get()
    if visit[src] == 1:
        continue
    else:
        visit[src] =1
    for dst in lines[src]:
        q.put(dst)

count = 0
for i in range(2 , cpt_cnt+1):
    if visit[i] == 1:
        count += 1

print (count)