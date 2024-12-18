import math
import copy


sampleFile1="./dades/sample9.txt"
dataFile = "./dades/input9.txt"



def readLine(filename):
    line=[]
    with open(filename) as file:
        for l in file:
            line+=(list(l.rstrip()))
    return line

def readList(filename):
    with open(filename) as file:
        lines = [line for line in file]
    return lines

def readMap(filename):
    with open(filename) as file:
        lines = [list(line.rstrip()) for line in file]
    return lines

def genCad(lenght,char):
    res=""
    for i in range(lenght):
        res+=char
    return res

def expand(data):
    res = []
    id=0
    gaps=[]
    limit = len(data)
    for i in range(limit):
        if i%2==0:
            #res+=genCad(int(data[i]),id)
            res +=[str(id) for a in range(int(data[i]))]
            id+=1
        else:
            gaps+=[a for a in range(len(res),len(res)+int(data[i]))]
            res+=["."]*int(data[i])
    return (res,gaps)

def expand2(data):
    res = []
    id=0
    files=[]
    limit = len(data)
    spaces=[]
    for i in range(limit):
        if i%2==0:
            #res+=genCad(int(data[i]),id)
            files.append((id,len(res),int(data[i])))
            res +=[str(id) for a in range(int(data[i]))]
            id+=1
            spaces+=["*"]*int(data[i])
        else:
            res+=["."]*int(data[i])
            spaces+=["."]*int(data[i])
    return (res,files,spaces)


def part1(data):
    (lex,gaps)= expand(data)
    idx = len(lex)-1
    for pos in gaps:
        if pos>=idx:
            break
        el = lex[idx]
        idx-=1
        while el == ".":
            el = lex[idx]
            idx-=1
        lex[pos]=el
        lex[idx+1]="."
    res=0
    for i in range(len(lex)):
        if lex[i]==".":
            break
        res += int(lex[i])*i
    print("PART1:",res)
    
def freeSpace(lex, idx):
    lenght=0
    while lex[idx]=="." and idx<len(lex):
        idx+=1
        lenght+=1
    return lenght


def part2(map):
    res=0
    (lex,files,spaces)= expand2(data)
    files.reverse()
    print("----------------")
    for file in files:
        (idx, filePosition, fileSize) = file
        spaceNeed = "".join(["."]*fileSize)
        freePos = "".join(spaces).find(spaceNeed)
        if freePos>=0 and freePos <filePosition:
            for i in range(fileSize):
                lex[freePos+i] = str(idx)
                lex[filePosition+i] = "."
                spaces[freePos+i] = "*"
            
    print(lex)  
    for i in range(len(lex)):
        if lex[i]!=".":
           res += int(lex[i])*i
    print("PART2:",res)

    
   
      
if __name__ == '__main__':
    #data = readLine(sampleFile1)
    #data = readMap(sampleFile1)
    
    #data = readList(dataFile)
    #data = readMap(dataFile)
    data = readLine(dataFile)
    
    
    
    part1(data)
    part2(data)
    
    
    