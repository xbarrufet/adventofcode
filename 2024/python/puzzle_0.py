import math
import copy


sampleFile1="./dades/sample9.txt"
dataFile = "./dades/input9.txt"


def readList(filename):
    with open(filename) as file:
        lines = [line for line in file]
    return lines

def readNap(filename):
    with open(filename) as file:
        lines = [list(line.rstrip()) for line in file]
    return lines



def part1(map):
    res=0
    print("PART1:",res)

def part2(map):
    res=0
    print("PART2:",res)

    
   
      
if __name__ == '__main__':
    data = readList(sampleFile1)
    #data = readMap(sampleFile1)
    
    #data = readList(dataFile)
    #data = readMap(dataFile)
    
    
    
    part1(data)
    part2(data)
    
    
    