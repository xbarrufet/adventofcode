import re
import aoc_tools as tools


cads = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

map =tools.readFileAsCharMap(4,test=False)
xpos=[]
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "X":
            xpos.append((i,j))
xmasCads = []
for x in xpos:
    for dir in cads:
        xmasCads.append([x,(x[0]+dir[0],x[1]+dir[1]),(x[0]+dir[0]*2,x[1]+dir[1]*2),(x[0]+dir[0]*3,x[1]+dir[1]*3)])

def cadValida(cad):
    for (i,j) in cad:
        if not( i>=0 and i<len(map) and j>=0 and j<len(map[0])):
            return False
    return True

res=0
for cad in xmasCads:
    if cadValida(cad):
        if map[cad[0][0]][cad[0][1]] == "X" and map[cad[1][0]][cad[1][1]] == "M" and map[cad[2][0]][cad[2][1]] == "A" and map[cad[3][0]][cad[3][1]] == "S":
            res+=1  
print(res)   
