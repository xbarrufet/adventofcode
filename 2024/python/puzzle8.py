import math
import copy


sampleFile1="./dades/sample8.txt"
dataFile = "./dades/input8.txt"


def readFile(filename):
    with open(filename) as file:
        lines = [list(line.rstrip()) for line in file]
    return lines

def antenasPermutations(antenas):
    perm = []
    for freq in antenas.keys():
        coords = antenas[freq]
        for i in range(len(coords)):
            for j in range(i+1,len(coords)):                            
                if (coords[j],coords[i]) not in perm:
                    perm.append((coords[i],coords[j]))
    return perm

def getAntinodes(ant1,ant2, height, width, locations):
    an1 = (ant1[0] + (ant1[0]-ant2[0]),ant1[1] + (ant1[1]-ant2[1]))
    an2 = (ant2[0] + (ant2[0]-ant1[0]),ant2[1] + (ant2[1]-ant1[1]))
    
    if an1[0]>=0 and an1[0]<height and an1[1]>=0 and an1[1]<width:
        if an1 not in locations:
            locations.append(an1)
    if an2[0]>=0 and an2[0]<height and an2[1]>=0 and an2[1]<width:
        if an2 not in locations:
            locations.append(an2)
    return locations

def getAntinodesPart2(ant1,ant2, height, width, locations):
    diffx1 = ant1[1]-ant2[1]
    diffx2 = ant2[1]-ant1[1]
    diffy1 = ant1[0]-ant2[0]
    diffy2 = ant2[0]-ant1[0]
    inGrid1=True
    inGrid2=True
    t=0
    while inGrid1 or inGrid2: 
        an1 = (ant1[0] + diffy1*t,ant1[1] + diffx1*t)
        an2 = (ant2[0] + diffy2*t,ant2[1] + diffx2*t)
        if an1[0]>=0 and an1[0]<height and an1[1]>=0 and an1[1]<width:
            if an1 not in locations:
                locations.append(an1)
        else:
            inGrid1=False    

        if an2[0]>=0 and an2[0]<height and an2[1]>=0 and an2[1]<width:
            if an2 not in locations:
                locations.append(an2)
        else:
            inGrid2=False    
        t+=1
    return locations

def lookForAntenas(map):
    antenas = {}
    for i in range(len(map)):
        for j in range(len(map[i])):
            ant = map[i][j]
            if ant != ".":
                if ant not in antenas.keys():
                    antenas[ant]=[(i,j)]
                else:
                    antenas[ant].append((i,j))
    return antenas



def part1(map):
    antenas = lookForAntenas(map)
    perms = antenasPermutations(antenas)
    locations = []
    for perm in perms:
       locations = getAntinodes(perm[0],perm[1],len(map),len(map[0]),locations) 
    print("PART1:",len(locations))

def part2(map):
    antenas = lookForAntenas(map)
    perms = antenasPermutations(antenas)
    locations = []
    for perm in perms:
       locations = getAntinodesPart2(perm[0],perm[1],len(map),len(map[0]),locations) 
    print("PART2:",len(locations))
  
    
    
#def part2(mapOrig, possibleBlockers):

      
if __name__ == '__main__':
    #map1 = readFile(sampleFile1)
    map1 =  readFile(dataFile)
    part1(map1)
    part2(map1)
    
    
    