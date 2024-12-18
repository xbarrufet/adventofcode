import math
import copy
import datetime

calculateStonesDict={}

def getCalculateStones(number, step):
    if "" + str(number) + "-" + str(step) in calculateStonesDict:
        return calculateStonesDict["" + str(number) + "-" + str(step)]
    else:
        return None
    
def setCalculateStones(number, step, value):
    calculateStonesDict["" + str(number) + "-" + str(step)] = value



def calculateNumberOfStones(value, step):
   
    if value ==0:
        if step<=1:
            setCalculateStones(0,step,1)
            return 1
        else:
            if getCalculateStones(0,step)!=None:
                res = getCalculateStones(0,step)
            else:
                res=calculateNumberOfStones(1,step-1)
            setCalculateStones(0,step,res)
            return res
    elif len(str(value))%2==0:
        if step<=1:
            setCalculateStones(value,step,2)
            return 2
        else:
            if getCalculateStones(value,step)!=None:
                res =  getCalculateStones(value,step)
            else:
                a = calculateNumberOfStones(int(str(value)[0:len(str(value))//2]),step-1)
                b = calculateNumberOfStones(int(str(value)[len(str(value))//2:]),step-1)
                res=a+b
            setCalculateStones(value,step,res)
            return res
    else:
        if step<=1:
            setCalculateStones(value,1,1)
            return 1
        else:
            if getCalculateStones(value,step)!=None:
                res=  getCalculateStones(value,step)
            else:
                res = calculateNumberOfStones(value*2024,step-1)
            setCalculateStones(value,step,res)
            return res
     
                
def part2(map, blinks):
    res=0
    stones = [int(st) for st in map]
    postion=0
    for stone in stones:
        res+=calculateNumberOfStones(stone,blinks)
    print("PART2:",res)

    
   
      
if __name__ == '__main__':
    #data= "2701 64945 0 9959979 93 781524 620 1".split(" ")
    data ="2701 64945 0 9959979 93 781524 620 1".split(" ")
    
    calculateStonesDict={}   
    a = datetime.datetime.now()
    part2(data,25)     
    b = datetime.datetime.now()
    print("TIME P1:",b-a)
    
    calculateStonesDict={}   
    b = datetime.datetime.now()
    part2(data,75)
    c = datetime.datetime.now()
    print("TIME P2:",c-b)
    
    
        
    
    