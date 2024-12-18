import math
import copy


sampleFile1="./dades/sample15-0.txt"
sampleFile2="./dades/sample15.txt"
dataFile = "./dades/input15.txt"



def readMap(filename):
    with open(filename) as file:
        lines=[]
        movs=[]
        for l in file:
            if "#" in l:
                lines.append(list(l.rstrip()))
            else:
                movs.extend(l.rstrip())
    return (lines, movs)


def getPosRobot(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j]=="@":
                return (i,j)

            
def getCell(map, pos):
    return map[pos[0]][pos[1]]


def copyCell(map, pos1, pos2):
    map[pos2[0]][pos2[1]]=map[pos1[0]][pos1[1]]

def getGPS(map,char="O"):
    gps=0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j]==char:
               gps+=100*i+j
    return gps
       
def printMap(map):
    for l in map:
        print("".join(l))


def nextCell(pos, movement):
    if movement=="^":
        return (pos[0]-1,pos[1])
    if movement=="v":
        return (pos[0]+1,pos[1])
    if movement=="<":
        return (pos[0],pos[1]-1)
    if movement==">":
        return (pos[0],pos[1]+1)


def movementAllowed(map,position,mov):
    nextPos = nextCell(position,mov)
    newCell = getCell(map,nextPos)
    if newCell=="O":
        return movementAllowed(map,nextPos,mov)
    elif getCell(map,nextPos)=="#":
        return False
    elif newCell=="[":
        if mov=="^" or mov=="v":
            return movementAllowed(map,nextPos,mov) and movementAllowed(map,(nextPos[0],nextPos[1]+1),mov)
        else:
            return movementAllowed(map,nextPos,mov)
    elif newCell=="]":
        if mov=="^" or mov=="v":
            return movementAllowed(map,nextPos,mov) and movementAllowed(map,(nextPos[0],nextPos[1]-1),mov)
        else:
            return movementAllowed(map,nextPos,mov)
    else: # "."
        return True
    
def doMovement(map,position,mov):
    nextPos = nextCell(position,mov)
    if getCell(map,nextCell(position,mov))=="O":
        doMovement(map,nextPos,mov)
    elif getCell(map,nextCell(position,mov))=="[":
        if mov=="^" or mov=="v":
            doMovement(map,nextPos,mov)
            doMovement(map,(nextPos[0],nextPos[1]+1),mov)
        else:
            doMovement(map,nextPos,mov)
    elif getCell(map,nextCell(position,mov))=="]":
        if mov=="^" or mov=="v":
            doMovement(map,nextPos,mov)
            doMovement(map,(nextPos[0],nextPos[1]-1),mov)
        else:
            doMovement(map,nextPos,mov)
            
    copyCell(map,position,nextPos)
    map[position[0]][position[1]]="."
        
    
            
def calculate(map,movements,char="O"):
    for m in movements:
        robot=getPosRobot(map)
        if movementAllowed(map,robot,m):
            doMovement(map,robot,m)
    gps=getGPS(map,char)
    print("RESULT",gps) 


def doubleMap(map):
    newMap = []
    for i in range(len(map)):
        newLine=[]
        for j in range(len(map[i])):
            if getCell(map,(i,j))=="O":
                newLine.extend(["[","]"])
            if getCell(map,(i,j))=="#":
                newLine.extend(["#","#"])
            if getCell(map,(i,j))==".":
                newLine.extend([".","."])
            if getCell(map,(i,j))=="@":
                newLine.extend(["@","."])
        newMap.append(newLine)
    return newMap




   
      
if __name__ == '__main__':
  
    (map,movs) = readMap(sampleFile1)
    calculate(map,movs)
    (map,movs) = readMap(sampleFile2)
    calculate(map,movs)
    (map,movs) = readMap(dataFile)
    calculate(map,movs)
    (map,movs) = readMap(dataFile)
    map = doubleMap(map)
    calculate(map,movs,"[")
    
    
    
    
    
    