import aoc_tools as tools


R=71
C=71
#R=7
#C=7
INI = 12

def printMaze(k,path=[]):
    for r in range(R):
        cad =""
        for c in range(C):
            if (c,r) in k:
                cad += "#"
            elif (c,r) in path:
                cad += "O"
            else:
                cad += "."
        print(cad)
        

l= tools.readFileAsList(18,True)
walls = []
for i in range(len(l)):
    pars= l[i].strip().split(",")
    walls.append((int(pars[0]), int(pars[1])))


def isValid(x,y,walls):
    return x>=0 and x<C and y>=0 and y<R and (x,y) not in walls


def buildPath(ox,oy,pred):
    path = [(ox,oy)]
    while ox!=0 and oy!=0:
        ox,oy = pred[(ox,oy)]
        path.append((ox,oy))
    return path


def buildMaze(walls):
    g = tools.Graph({})
    print("walls:",len(walls))
    for y in range(R):
        for x in range(C):
            if (x,y) in walls:
                continue
            if isValid(x+1,y,walls):  
                g.add_edge((x,y),(x+1,y),1)
            if isValid(x-1,y,walls):
                g.add_edge((x,y),(x-1,y),1)
            if isValid(x,y+1,walls):
                g.add_edge((x,y),(x,y+1),1)
            if isValid(x,y-1,walls):
                g.add_edge((x,y),(x,y-1),1)
    counter=0
    for n in g.graph.keys():
        counter += len(g.graph[n])
    return g

# for i in range(len(walls)):
#     if i>0:
#         print(walls[i-1])
#     partial_walls = walls[:i]
#     gr=buildMaze(partial_walls)
    
#     d= gr.shortest_distances((0,0))
#     if  d[(C-1,R-1)]>R*C:
#        print("RES:" , walls[i-1])
#        break
#     print("----", d[(C-1,R-1)], "----")
    
    

    return g
def part2(walls):
    ini = 1024
    partial_walls = walls[:ini]
    gr=buildMaze(partial_walls)
    d= gr.shortest_distances((0,0))
    path = gr.getPredecessorsPath((C-1,R-1))
    for i in range(ini,len(walls)):
        print("i:",i, end="\r") 
        newWall=walls[i]
        if newWall in path:
            print("wall in path:",newWall)
            gr.remove_edge((newWall[0],newWall[1]-1),newWall)
            gr.remove_edge((newWall[0],newWall[1]+1),newWall)
            gr.remove_edge((newWall[0]-1,newWall[1]),newWall)
            gr.remove_edge((newWall[0]+1,newWall[1]),newWall)
            d = gr.shortest_distances((0,0))
            if d[(C-1,R-1)]>R*C:
                print("RES:",newWall)
                break
            path = gr.getPredecessorsPath((C-1,R-1))
        
    return d[(C-1,R-1)]

part2(walls)