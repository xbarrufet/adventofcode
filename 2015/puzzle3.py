import aoc_tools as tools

cad = tools.readFileAsString(3,True)

dirs = {'^':(1,0), 'v':(-1,0), '>':(0,1), '<':(0,-1)}

seen = set()
r=0
c=0
seen.add((r,c))
for d in list(cad):
    (dr,dc) = dirs[d]
    r += dr
    c += dc
    if (r,c) not in seen:
        seen.add((r,c))
print(len(seen))

seen = set()
r=0
c=0
rr=0
rc=0
seen.add((r,c))
for i in range(len(cad)):
    if i % 2 == 0:
        (dr,dc) = dirs[cad[i]]
        r += dr
        c += dc
        if (r,c) not in seen:
            seen.add((r,c))
    else:
        (dr,dc) = dirs[cad[i]]
        rr += dr
        rc += dc
        if (rr,rc) not in seen:
            seen.add((rr,rc))
print(len(seen))
    