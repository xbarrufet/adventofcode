import math
import copy


sampleFile1="./dades/sample10.txt"
dataFile = "./dades/input10.txt"





def readMap(filename):
    with open(filename) as file:
        lines = [list(line.rstrip()) for line in file]
    return lines



def nextStep(data,i,j,nextHeight,maxHeight,maxWidth):
  
    if int(nextHeight)>9:
        return [[(i,j)]]
    paths = []
    if i>0 and data[i-1][j]==nextHeight:
        paths.append((i-1,j))
    if j<maxWidth-1 and data[i][j+1]==nextHeight:
        paths.append((i,j+1))
    if i<maxHeight-1 and data[i+1][j]==nextHeight:
        paths.append((i+1,j))
    if j>0 and data[i][j-1]==nextHeight:
        paths.append((i,j-1))
    value=0
    trails =[]
    if(len(paths)==0):
        return None
    for p in paths:
        closedPaths=nextStep(data,p[0],p[1],str(int(nextHeight)+1),maxHeight,maxWidth)
        if closedPaths is not None:
            for closedPath in closedPaths:
                closedPath.append((i,j))
                trails.append(closedPath) 
    return trails




def part1(data):
    res=0
    maxHeight = len(data)
    maxWidth = len(data[0])
    trails = []
    for i in range(maxHeight):
        for j in range(maxWidth):
            if data[i][j]=="0":
               trails+=nextStep(data,i,j,"1",maxHeight,maxWidth)
   
    resTrails =[]
    for trail in trails:
        trailHead = [trail[-1],trail[0]]
        if trailHead not in resTrails:
            resTrails.append(trailHead)
    numTrails={}
    for trail in resTrails:
        orig=str(trail[0])
        if orig in numTrails:
            numTrails[orig]+=1
        else:
            numTrails[orig]=1
    print(numTrails)
    print("PART1:",len(resTrails))
    


def part2(map):
    res=0
    maxHeight = len(data)
    maxWidth = len(data[0])
    trails = []
    for i in range(maxHeight):
        for j in range(maxWidth):
            if data[i][j]=="0":
               trails+=nextStep(data,i,j,"1",maxHeight,maxWidth)
    print("PART2:",len(trails))

    
   
      
if __name__ == '__main__':
    data = readMap(sampleFile1)
    
    data = readMap(dataFile)
    part1(data)
    part2(data)
    
    
    