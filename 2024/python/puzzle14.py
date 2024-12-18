import numpy as np
import math
import copy
from functools import reduce
from operator import mul
import re
import pygame, sys


TIME=100
#NUMROWS = 7
#NUMCOLS =11
NUMROWS = 103
NUMCOLS =101


def readList(filename):
    with open(filename) as file:
        lines = [line for line in file]
    return lines


def quadrant(positions):
    quadrants=[0]*4
    qrow1 = (NUMROWS//2-1)
    qrow2 = qrow1+2
    qcol1 = (NUMCOLS//2-1)
    qcol2 = qcol1+2
    
    
    for x in positions:
        if x[0]<=qcol1 and x[1]<=qrow1:
            quadrants[0]+=1
        elif x[0]<=qcol1 and x[1]>=qrow2:
            quadrants[1]+=1
        elif x[0]>=qcol2 and x[1]<=qrow1:
            quadrants[2]+=1
        elif x[0]>=qcol2 and x[1]>=qrow2:   
            quadrants[3]+=1
    print(quadrants)
    return reduce(mul, quadrants) 
        
        

def matrius():
    #res = np.fromregex('dades/sample14.txt', r'[+-]?\d+', [('', int)]*4).view(int).reshape(-1,4).T
    res = np.fromregex('dades/input14.txt', r'[-]?\d+', [('', int)]*4).view(int).reshape(-1,4).T
    P =np.vstack((res[0],res[1])).T
    V =np.vstack((res[2],res[3])).T
    divs = np.array([NUMCOLS,NUMROWS])
    res = np.mod(P+V*TIME,divs).tolist()
    res = quadrant(res)
    print(res)

#206758656

def parser():
    p_values = []
    v_values = []
    #list = readList("dades/sample14.txt")
    list = readList("dades/input14.txt")
    pattern = r'p=(-?\d+),(-?\d+)\s*v=(-?\d+),(-?\d+)'
    # Find all matches in the file content
    # Extract 'p' and 'v' from matches
    for line in list:
        matches = re.findall(pattern, line)
        for match in matches:
            p = [int(match[0]), int(match[1])] # Create tuple for 'p'
            v = [int(match[2]), int(match[3])] # Create tuple for 'v'
            p_values.append(p)
            v_values.append(v)
    return (p_values,v_values)
    
def part1_timeskip(p_values,v_values,time,rows,cols):
    for i in range(len(p_values)):
        p_values[i][0] = (p_values[i][0]+v_values[i][0] * time) % cols
        p_values[i][1] = (p_values[i][1]+v_values[i][1] * time) % rows
    return p_values


def moveTime(P,V,divs,time):
    P = P+V*time
    P = np.mod(P,divs)
    return P

def calculateDistances(P):
    plist = P.tolist()
    sumd = 0
    for i in range(len(plist)):
        for j in range(i+1,len(plist)):
            sumd+= math.sqrt((plist[i][0]-plist[j][0])**2 + (plist[i][1]-plist[j][1])**2)
    return sumd

def distances():
    res = np.fromregex('dades/input14.txt', r'[-]?\d+', [('', int)]*4).view(int).reshape(-1,4).T
    #res = np.fromregex('dades/sample14.txt', r'[-]?\d+', [('', int)]*4).view(int).reshape(-1,4).T
    P =np.vstack((res[0],res[1])).T
    V =np.vstack((res[2],res[3])).T
    divs = np.array([NUMCOLS,NUMROWS])
    counter = 1
    dist=8519949
    times=[]
    P=moveTime(P,V,divs,10000)
    for i in range(20000,50000):
         P=moveTime(P,V,divs,1)
         #distNew = calculateDistances(P)
         distNew =  distNew = np.linalg.norm(P - P[:,None], axis=-1).sum()
         if distNew<dist:
             dist=distNew
             times.insert(0,[i,dist])
         print("time: ",i,end="\r")   
    print(times[:100])

def part2():
    counter = 635
    pygame.init()
    res = np.fromregex('dades/input14.txt', r'[-]?\d+', [('', int)]*4).view(int).reshape(-1,4).T
    P =np.vstack((res[0],res[1])).T
    V =np.vstack((res[2],res[3])).T
    divs = np.array([NUMCOLS,NUMROWS])
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    rX= 640/NUMCOLS
    rY= 480/NUMROWS
    P=moveTime(P,V,divs,counter)
    position = P.tolist()
    goon = False
    while True:
        screen.fill((0,0,0))
        # prunt counter
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render(str(counter), True, (0,200,0),(0,0,200))
        textRect = text.get_rect()
        textRect.center = (320, 240)
        screen.blit(text, textRect)
          
        if goon:
            counter=counter+1
            P=moveTime(P,V,divs,1)
            position = P.tolist()
        for pos in position:
            pygame.draw.circle(screen, (200,200,200), (pos[0]*rX,pos[1]*rY), rX/2)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #goon = not goon
                counter=counter+1
                P=moveTime(P,V,divs,1)
                position = P.tolist()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #pygame.time.wait(100)
if __name__ == '__main__':
    # p=[]
    # v=[]
    # (p,v) = parser()
    # p=part1_timeskip(p,v,TIME,NUMROWS,NUMCOLS)
    # print(p)
    # res = quadrant(p)
    
    # print(res)
    # matrius()

    #pygame.init()
    part2()
    #distances() 
    

#220971520

# 10000
# [[6354, 4259974.2673942065], [193, 5381753.753198663], [92, 5502288.088425143], [71, 5759819.15860951], [40, 6392654.329123341], [38, 6455863.188073547], [12, 6461207.713192955], [2, 6521395.600162018], [1, 6685625.807273917], [0, 6734841.444099191]]

# 20000
# [[16757, 4259974.2673942065], [10596, 5381753.753198663], [10293, 5476034.248293132], [10192, 5564309.028807989], [10091, 5595859.282329768], [10062, 5694555.639802904], [10031, 6445795.762444049], [10011, 6498963.000304836], [10000, 6586740.59358606]