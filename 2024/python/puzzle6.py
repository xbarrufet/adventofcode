import math
import copy


sampleFile1="./dades/sample6.txt"
dataFile = "./dades/input6.txt"


def readFile(filename):
    with open(filename) as file:
        lines = [list(line.rstrip()) for line in file]
    return lines

def lookForPosition(map):
    position = [-1,1]
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j]=="^":
                position = [i,j]
    return position

def countX(map):
    res=0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j]=="X":
                res+=1
    return res

def moveForward(position, direction):
    if direction=="N":
        return [position[0]-1,position[1]]
    if direction=="S":
        return [position[0]+1,position[1]]
    if direction=="W":
        return [position[0],position[1]-1]
    if direction=="E":
        return [position[0],position[1]+1]
    
def turnRight(direction):
    if direction=="N":
        return "E"
    if direction=="S":
        return "W"
    if direction=="W":
        return "N"
    if direction=="E":
        return "S"   

def isPositionInMap(position, map):
    if position[0]<0 or position[0]>=len(map):
        return False
    if position[1]<0 or position[1]>=len(map[0]):
        return False
    return True

def isPositionBlocked(position, map):
    if map[position[0]][position[1]]=="#":
        return True
    return False


def characterDirection(direction):
    if direction=="N":
        return "^"
    if direction=="S":
        return "v"
    if direction=="W":
        return "<"
    if direction=="E":
        return ">"


def part1(map):
    position = lookForPosition(map)
    direction = "N"
    steps=[]
    isOut=False
    while not isOut:
        map[position[0]][position[1]]="X"
        steps.append((direction, position))
        newPosition = moveForward(position, direction) 
        if not isPositionInMap(newPosition, map):
            isOut=True
        elif map[newPosition[0]][newPosition[1]]=="#":
            direction = turnRight(direction)
        else:
            position = newPosition     
            
    print("PART1: ",countX(map))
    return steps
    
def isPreviousAt90Degress(position, direction, map):
    prevDir = map[position[0]][position[1]]
    if prevDir=="^" and direction=="W":
        return True
    if prevDir=="v" and direction=="E":
        return True
    if prevDir==">" and direction=="N":
        return True
    if prevDir=="<" and direction=="S":
        return True
    return False
            
    
def part2(mapOrig, possibleBlockers):

    positionOrig = lookForPosition(mapOrig)
    blockers = []
    for posBlocker in possibleBlockers:
            map= copy.deepcopy(mapOrig)
            map[posBlocker[0]][posBlocker[1]]="#"
            position = positionOrig
            direction = "N"
            isOut=False
            steps=[]
          
            while not isOut and (direction,position) not in steps:
                map[position[0]][position[1]]=characterDirection(direction)
                steps.append((direction, position))
                newPosition = moveForward(position, direction) 
                if not isPositionInMap(newPosition, map):
                    isOut=True
                    break
                if map[newPosition[0]][newPosition[1]]=="#":
                    direction = turnRight(direction)
                else:
                    position = newPosition                    
            if(not isOut):
                if posBlocker not in blockers:
                    blockers.append(posBlocker)
                
    print("PART2: ",len(blockers))
    print("PART2: ",blockers)
    
if __name__ == '__main__':
    map1 = readFile(sampleFile1)
    map1 =  readFile(dataFile)
    steps=part1(map1)
    
    possibleBlockers = [moveForward(step[1],step[0]) for step in steps]
    #map2 = readFile(sampleFile1)
    map2 =  readFile(dataFile)
    part2(map2,possibleBlockers[:-1])
    
    