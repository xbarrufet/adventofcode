sampleFile1="./dades/sample2.txt"
dataFile = "./dades/input2.txt"




def readData(filename):
    with open(filename) as file:
        return [line.rstrip().split(" ") for line in file]
    
    
def isSafe(li):
    subs = [li[i] - li[i+1] for i in range(len(li)-1) ]
    return all(item<0 and item>-4 for item in subs) or all(item>0 and item<4 for item in subs)
    
def part1(lines):
    safe=0
    for l in lines:
        li =[int(item) for item in l]
        if isSafe(li):
           safe+=1
    print(safe)
       
def part2(lines):
    safe=0
    for l in lines:
        li =[int(item) for item in l]
        isLineSafe=False
        for i in range(len(li)):
            li_aux = li[:i]+li[i+1:]
            if isSafe(li_aux):
               isLineSafe=True
        if isLineSafe:
            safe+=1
    print(safe)
    
if __name__ == '__main__':
    #list = readData(sampleFile1)
    list = readData(dataFile)
    part1(list)
    part2(list)

    