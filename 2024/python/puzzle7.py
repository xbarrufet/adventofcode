from itertools import product
import copy




sampleFile1="./dades/sample7.txt"
dataFile = "./dades/input7.txt"



def readFile(filename):
    with open(filename) as file:
        lines = [line for line in file]
    return lines


def operate(perm, param):
    #filter | symbol
    perm = list(perm)
    # operate rest of symbols
    p1 = param[0]
    for i in range(len(perm)):
        p2 = param[i+1]
        if perm[i] == "+":
            p1 += p2
        elif perm[i] == "|":
            p1 = int(str(p1)+ str(p2))
        else:
            p1 *= p2
    return p1

def part1(lines):
    symbols = ["+", "*"]
    res = []
    for line in lines:
       opers = line.split(":")
       value = int(opers[0])
       if value == 292:
           a=2
       parameters =[int(num) for num in opers[1].strip().split(" ")]
       perm = [p for p in product(symbols, repeat=len(parameters)-1)]
       for p in perm:
           if operate(p, parameters) == value:
               if value not in res:
                   print(value)
                   res.append(value)
    return sum(res)

def part2(lines):
    symbols = ["+", "*","|"]
    res = []
    for line in lines:
       opers = line.split(":")
       value = int(opers[0])
       if value == 292:
           a=2
       parameters =[int(num) for num in opers[1].strip().split(" ")]
       perm = [p for p in product(symbols, repeat=len(parameters)-1)]
       for p in perm:
           if operate(p, copy.deepcopy(parameters)) == value:
               if value not in res:
                   print(value)
                   res.append(value)
    return sum(res)

if __name__ == '__main__':
    #lines = readFile(sampleFile1)
    lines = readFile(dataFile)
    print("P1",part1(lines))
    print("P2",part2(lines))