import math
import copy


sampleFile1="./dades/sample12.txt"
dataFile = "./dades/input12.txt"


def readList(filename):
    with open(filename) as file:
        lines = [line for line in file]
    return lines

def readMap(filename):
    with open(filename) as file:
        lines = [list(line.rstrip()) for line in file]
    return lines




def getNeighbours(map, i,j,plant, visited, areaPlant):
    
   
    visited.append((i,j))
    
            
    res=[]
    fencesCell=""
    if i>0 and map[i-1][j]==plant:
        res.append((i-1,j))
    else:
        fencesCell+="N"     
            
    if j>0 and map[i][j-1]==plant:
         res.append((i,j-1))
    else:
        fencesCell+="W"
            
            
    if i<len(map)-1 and map[i+1][j]==plant:
         res.append((i+1,j))
    else:
        fencesCell+="S"
            
    if j<len(map[i])-1 and map[i][j+1]==plant:
         res.append((i,j+1))
    else:
        fencesCell+="E"
        
    if(((i,j),fencesCell) not in areaPlant):
            areaPlant.append(((i,j),fencesCell))

    for n in res:
        if n not in visited:
            (visited, areaPlant) = getNeighbours(map,n[0],n[1],plant,visited,areaPlant)
    return (visited, areaPlant)


def fencesSides(areaMap):
    res=""
    fences=0
    for i in range(len(areaMap)):
        for j in range(len(areaMap[i])):
            if areaMap[i][j]!="":
                if "N" in areaMap[i][j] and (j==0 or "N" not in areaMap[i][j-1]):
                    fences+=1
                if "W" in areaMap[i][j] and (i==0 or "W" not in areaMap[i-1][j]):
                    fences+=1
                if "S" in areaMap[i][j] and (j==0 or "S" not in areaMap[i][j-1]):
                    fences+=1
                if "E" in areaMap[i][j] and (i==0 or "E" not in areaMap[i-1][j]):
                    fences+=1
    return fences



def part1(map):
    res=0
    totalvisited=[]
    
    for i in range(len(map)):
        for j in range(len(map[i])):
            if (i,j) not in totalvisited:
                visited=[]
                area=0
                fences=0
                (visited, fences) = getNeighbours(map,i,j,map[i][j],visited,fences)
                totalvisited+=visited
                res +area*fences
    print("PART1:",res)
        
    
    
def part2(map):
    res=0
    totalvisited=[]
    totalFencesAreas = []
    totalAreaPlants=[]

    for i in range(len(map)):
        for j in range(len(map[i])):
            if (i,j) not in totalvisited:
                visited=[]
                plant = map[i][j]
                (visited, areaPlant) = getNeighbours(map,i,j,map[i][j],visited,[])
                totalAreaPlants.append(areaPlant)
                totalvisited+=visited
    totalFences=0
    for a in totalAreaPlants:
        mapArea=[[""]*len(map[0]) for i in range(len(map))]
        for p in a:
            mapArea[p[0][0]][p[0][1]]=p[1]
        totalFences += fencesSides(mapArea)*len(a)
    print(totalFences)

   
      
if __name__ == '__main__':
    #data = readMap(sampleFile1)
    data = readMap(dataFile)
    
    #part1(data)
    part2(data)
    
    
    