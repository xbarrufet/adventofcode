import math
import copy
import numpy as np


sampleFile1="./dades/sample13.txt"
dataFile = "./dades/input13.txt"

def readList(filename):
    with open(filename) as file:
        lines = [line for line in file]
    return lines

def getButton(line):
    aux = line.split("+")
    return [int(aux[1][0:2]),int(aux[2][0:2])]

def getPrize(line):
    aux = line.split("=")
    return [int(aux[1].split(",")[0]),int(aux[2])]

    

def solving_equation(buttonA, buttonB, prize):
    res = []
    A = np.matrix([[buttonA[0],buttonB[0]],[buttonA[1],buttonB[1]]])
    B= np.matrix([[prize[0]],[prize[1]]])
    sol= np.linalg.solve(A,B).round().astype(int)
    R=np.all(np.squeeze(A@sol==B),1).tolist()
    if R[0][0]:
        return sol.tolist()
    else:
        return []
    #    print(sol)
    

def solving(buttonA, buttonB, prize):
        pulls=[0,0]
        winnerPull=[100,100]      
        while pulls[0]<=100:
            while pulls[1]<=100:
                if pulls[0]*buttonA[0] + pulls[1]*buttonB[0]==prize[0] and pulls[0]*buttonA[1]+pulls[1]*buttonB[1]==prize[1]:
                    if pulls[0]*3+pulls[1]*1<winnerPull[0]*3+winnerPull[1]*1:
                        winnerPull=[pulls[0],pulls[1]]
                pulls[1]=pulls[1]+1
            pulls[0]=pulls[0]+1
            pulls[1]=0
        return winnerPull



def part1(data):
    cont=0
    res=0
    while cont<len(data):
        buttonA = getButton(data[cont])
        buttonB = getButton(data[cont+1])
        prize = getPrize(data[cont+2])
        cont=cont+4
        winnerPull=solving(buttonA,buttonB,prize)
        if winnerPull[0]<100 or winnerPull[1]<100:
            res += winnerPull[0]*3+winnerPull[1]*1
    print("PART1: ", res)
    
def part2(data):
    cont=0
    res=0
    while cont<len(data):
        buttonA = getButton(data[cont])
        buttonB = getButton(data[cont+1])
        prize = getPrize(data[cont+2])
        prize = [prize[0]+10000000000000,prize[1]+10000000000000]
        sol = solving_equation(buttonA,buttonB,prize)
        if len(sol)>0:
            res += sol[0][0]*3+sol[1][0]
        cont=cont+4
    print(res)

def copied():
    M = np.fromregex('in.txt', r'\d+', [('', int)]*6).view(int).reshape(-1,3,2).swapaxes(1,2)
    print(M)
    for p in 0, 1e13:
        print("p:",p)
        S = M[..., :2]
        P = M[..., 2:] + p
        R = np.linalg.solve(S, P).round().astype(int)
        print(*R.squeeze() @ [3,1] @ (S @ R == P).all(1))

      
if __name__ == '__main__':
    data = readList(sampleFile1)
    #data = readList(dataFile)
    #part1(data)
    #part2(data)
    copied()

#108528956728655
