import aoc_tools as tools
import re
import math

s = tools.readFileAsString(1,True)

pis=0
l = list(s)
for i in range(len(l)):
    if l[i] == '(':
        pis+=1
    elif l[i] == ')':
        pis-=1
    if pis==-1:
        print(i+1)
        break    

