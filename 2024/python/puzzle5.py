import math


sampleFile1="./dades/sample5.txt"
dataFile = "./dades/input5.txt"


def readFile(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    section=False
    updates = []
    for line in lines:
        if line=="":
            section=True
        else:
            if section:
                updates.append(line)
    return (lines, updates)

def generatePermutations(updates):
    if len(updates)==1:
        return []
    else:
        head = updates[0]
        tail = updates[1:]
        res=[]
        for n in tail:
            res.append("" + head + "|" + n)
        return res+generatePermutations(tail)
    
    
def generateUpdatePermutations(updates,lines):
        perm=[]
        res=[]
        for u in updates:
            perm+=["" + u + "|" + el for el in updates if el != u]
        res = [el for el in perm if el in lines]
        return res


def updaeExist(update, lines):
    for u in update:
        if u not in lines:
            return False
    return True
    
def orderUpdates(update,perms):
    orderedList = [0]*len(update)
    for u in update:
        occurs = [el for el in perms if el.startswith("" + u + "|")]
        orderedList[len(occurs)]=u
    return [el for el in orderedList if el != 0]  


def part1(lines, updates):
    perms = []
    updateOk = []
    updateNOk = []
    for update in updates:
        updateList = update.split(",")
        perms = generatePermutations(updateList)
        if updaeExist(perms,lines):
            updateOk.append(updateList)
        else:
            updateNOk.append(updateList)
    res=0
    for l in updateOk:
        res+=int(l[math.floor(len(l)/2)])
    print(res)
    return updateNOk
    
def part2(lines, updates):
    res=0
    for update in updates:
        perms = generateUpdatePermutations(update,lines)
        orderedList = orderUpdates(update, perms)
        print(orderedList)
        res+=int(orderedList[math.floor(len(orderedList)/2)])    
    print(res)
    
    
if __name__ == '__main__':
    #(lines, updates) = readFile(sampleFile1)
    (lines, updates) = readFile(dataFile)
    
    updateNOK = part1(lines, updates)
    part2(lines, updateNOK)
    