import aoc_tools as tools
import re
import math


l = tools.readFileAsList(2,True)
#l =["2x3x4","1x1x10"]
res=0
ribbon=0    
for d in l:
    dl = d.split('x')
    l =int(dl[0])
    w =int(dl[1])
    h =int(dl[2])
    res += 2*l*w + 2*w*h + 2*h*l+min(l*w,w*h,h*l)
    ribbon += 2 * (l + w + h - max(l, w, h))+ l * w * h
print(ribbon)
    
