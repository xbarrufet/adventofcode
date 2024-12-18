import math
import aoc_tools as tools

sampleFile1="./dades/sample1.txt"
dataFile = "./dades/input1.txt"




def readData(filename):
    col1=[]
    col2=[]
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            col1.append(line.split("   ")[0])
            col2.append(line.split("   ")[1])
    return col1,col2

def part1(col1,col2):
    col1.sort() 
    col2.sort()
    print(sum([abs(int(x)-int(y)) for x,y in zip(col1,col2)]))
    
def part2(col1,col2):
    freq = [col2.count(x)*int(x) for x in col1]
    print(sum(freq))

if __name__ == '__main__':
    #col1,col2 = readData(sampleFile1)
    col1,col2 = readData(dataFile)
    part1(col1,col2)
    part2(col1,col2)
   
        
    