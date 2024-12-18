import aoc_tools as tools
import math
import sys

nextPos = {"^":(-1,0),">":(0,1),"v":(1,0),"<":(0,-1)}
turnDirectionLeft = {"^":"<","<":"v","v":">",">":"^"}
turnDirectionRight = {"^":">",">":"v","v":"<","<":"^"}
turnDirectionBack = {"^":"v",">":"<","v":"^","<":">"}


def sumPos(a,b):
    return (a[0]+b[0],a[1]+b[1])    

def isValidPos(map, pos):
    return pos[0]>=0 and pos[0]<len(map) and pos[1]>=0 and pos[1]<len(map[0]) and getCell(map, pos) != "#"

def getCell(map, pos):
    return map[pos[0]][pos[1]]


def posToStr(pos,direction):
    return str(pos[0])+","+str(pos[1])+","+direction

def strToPos(str):
    sp = str.split(",")
    return (int(sp[0]),int(sp[1]),sp[2])  

def createGraph(map):
    graph = tools.Graph()
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] != "#":
                graph.add_edge(posToStr((i,j),">"), posToStr((i,j),"<"),2000)
                graph.add_edge(posToStr((i,j),">"),posToStr((i,j),"v"),1000)
                graph.add_edge(posToStr((i,j),">"),posToStr((i,j),"^"),1000)
                graph.add_edge(posToStr((i,j),"<"), posToStr((i,j),">"),2000)
                graph.add_edge(posToStr((i,j),"<"),posToStr((i,j),"v"),1000)
                graph.add_edge(posToStr((i,j),"<"),posToStr((i,j),"^"),1000)
                graph.add_edge(posToStr((i,j),"v"), posToStr((i,j),">"),1000)
                graph.add_edge(posToStr((i,j),"v"),posToStr((i,j),"<"),1000)
                graph.add_edge(posToStr((i,j),"v"),posToStr((i,j),"^"),2000)
                graph.add_edge(posToStr((i,j),"^"), posToStr((i,j),">"),1000)
                graph.add_edge(posToStr((i,j),"^"),posToStr((i,j),"<"),1000)
                graph.add_edge(posToStr((i,j),"^"),posToStr((i,j),"v"),2000)
                frontUp = sumPos((i,j),nextPos["^"])
                if isValidPos(map,frontUp):
                    graph.add_edge(posToStr((i,j),"^"),posToStr(frontUp,"^"), 1)
                frontLeft = sumPos((i,j),nextPos["<"])
                if isValidPos(map,frontLeft):
                    graph.add_edge(posToStr((i,j),"<"),posToStr(frontLeft,"<"), 1)
                frontRight = sumPos((i,j),nextPos[">"])
                if isValidPos(map,frontRight):
                    graph.add_edge(posToStr((i,j),">"),posToStr(frontRight,">"), 1)
                frontDown = sumPos((i,j),nextPos["v"])
                if isValidPos(map,frontDown):
                    graph.add_edge(posToStr((i,j),"v"),posToStr(frontDown,"v"), 1)
    return graph


def startPosition(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "S":
                return (i,j)
    return None

def endPosition(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "E":
                return (i,j)
    return None



def test2():
    gr 

if __name__ == '__main__':
    #9444
    #7036
    sys.setrecursionlimit(100000)    
    data = tools.readFileAsCharMap(16,False)
    maze = createGraph(data)
    distances = maze.shortest_distances(posToStr(startPosition(data),">"))
    print(distances[posToStr(endPosition(data),">")])
    print(distances[posToStr(endPosition(data),"^")])
    paths = maze.minimalPath(posToStr(startPosition(data),">"),posToStr(endPosition(data),"^"),distances[posToStr(endPosition(data),"^")])
        
   
    seats =[]
    for path in paths:
        for node in path:
            (i,j,direction)=strToPos(node)
            if (i,j) not in seats:
                seats.append((i,j))
    print(len(seats))
    
    
    
    