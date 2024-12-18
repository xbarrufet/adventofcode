import aoc_tools as tools
import heapq

data = tools.readFileAsCharMap(16,True)
R=len(data)
C=len(data[0])  

DIRS =[(-1,0),(0,1),(1,0),(0,-1)] #u r d l  
for r in range(R):
    for c in range(C):
        if data[r][c] == "S":
            sr,sc=r,c
        if data[r][c] == "E":
            er,ec = r,c

Q=[]
SEEN=set()
heapq.heappush(Q,(0,sr,sc,1))
while Q:
    d,r,c,dir = heapq.heappop(Q)
    if r==er and c==ec:
        print(d)
        break
    if (r,c,dir) in SEEN:   
        continue
    SEEN.add((r,c,dir))
    dr,dc = DIRS[dir]
    rr,cc = r+dr,c+dc
    if data[rr][cc] != "#":
        heapq.heappush(Q,(d+1,rr,cc,dir))
    heapq.heappush(Q,(d+1000,r,c,(dir+1)%4))
    heapq.heappush(Q,(d+1000,r,c,(dir+3)%4))
    

words = [(1,'A'),(4,'D'),(3,"C"),(2,"B")]
Q=[]
for x in words:
    heapq.heappush(Q,x) 
while Q:
    print(heapq.heappop(Q))
