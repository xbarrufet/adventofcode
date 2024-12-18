import math

def combo(op, regs):
    if op<4:
        res= op
    else:
        res= regs[op-4]
    return res

def run(regs,program):
    REGS = [regs[0],regs[1],regs[2]]
    IP=0
    OUT=[]

    while IP<len(program):
        instr=program[IP]
        op=program[IP+1]
        if(instr!=3 or REGS[0]==0):
            IP=IP+2
        if instr==0:
            REGS[0]= math.floor(REGS[0]/(pow(2,combo(op,REGS))))
        elif instr==1:
            REGS[1] = REGS[1] ^ op
        elif instr==2:
            REGS[1] =combo(op,REGS)%8
        elif instr==3:
            IP =IP if REGS[0] == 0 else op
        elif instr==4:
            REGS[1] =REGS[1] ^ REGS[2]
        elif instr==5:
            OUT.append(combo(op,REGS)%8)
        elif instr==6:
            REGS[1]= math.floor(REGS[0]/(pow(2,combo(op,REGS))))
        elif instr==7:
            #REGS[2]=math.floor(REGS[0]/(pow(2,combo(op,REGS))))
            REGS[2]=math.floor(REGS[0]/(pow(2,combo(op,REGS))))%8
    return (REGS, OUT)


program =   [2,4,1,7,7,5,0,3,4,4,1,7,5,5,3,0]


 
    #[(2,4),     (1,7),     (7,5),      (0,3),    (4,4),      (1,7),   (5,5),     (3,0)])
    #B= A%7 ,   B=7-B,   C=(A/2 ^B).    A=A/8     B=B XOR C   B=7-B    print(B)   start(0)




bins = [0,1,2,3,4,6,13,28]
# for b in bins:
#      print(b,'{0:06b}'.format(b))
#      print(b,'{0:03b}'.format(b))
     
rega= int("1000",2)
rega=800000
print("8:" , rega)
(regs, out) = run([rega,0,0],program)
print(out)
# rega= int("010",2)
# print(rega)
# (regs, out) = run([rega,0,0],program)
# print(out)

def inv(s):
    s=list(s)
    res=[1 if x=='0' else 0 for x in s]
    return res

def xor(s1,s2):
    return [1 if x1!=x2 else 0 for x1,x2 in zip(s1,s2)] 


def exec(n):
    out = []
    while True:
        b = (n % 8) ^7 
        c = n >> b
        out.append((b ^ c ^7) % 8)
        n = n // 8
        if n == 0: break
    return out

program = [2,4,1,7,7,5,0,3,4,4,1,7,5,5,3,0]

def findSlot(program,prev=0,leni=0):
    res=None
    if leni>len(program):
        return prev
    for i in range(8):
        out = exec(8*prev+i)
        print("REG_A:",8*prev+i, out)
        if out==program:
            print("found:",8*prev+i )
            break
        o = program[-leni:]
        if len(out)== leni and  out == program[-leni:]:
            res =  findSlot(program,8*prev+i,leni+1)
            if res is not None:
                continue
    
    return res

#a=findSlot(program,0,1)
#print("res:", a)
# def exec(n):
#     while True:
#         b = (n % 8) ^ 1
#         c = n >> b
#         yield (b ^ c ^ 4) % 8
#         n = n // 8
#         if n == 0: break


# def discover_input(program, prev=0):
#      print("prev",prev)
#      if not program: yield prev; return
#      for i in range(8):
#          if next(exec(8*prev+i)) == program[-1]:
#              yield from discover_input(program[:-1], 8*prev+i)

# print("------")
# for x in discover_input([2,4,1,7,7,5,0,3,4,4,1,7,5,5,3,0]):
#     print(x)    
# for i in range(pow(8,15),pow(8,16)):
# print("i:",i,end="\r")
# out = exec(i)
# if out == program:
#     print("found:",i)
    
#     break

import re

a, b, c, *prog = map(int, re.findall(r'\d+', 
                     open('in.txt').read()))

def eval(a, b, c, i=0, R=[]):
    while i in range(len(prog)):
        C = {0:0,1:1,2:2,3:3,4:a,5:b,6:c}

        match prog[i:i+2]:
            case 0, op: a = a >> C[op]
            case 1, op: b = b ^ op
            case 2, op: b = 7 & C[op]
            case 3, op: i = op-2 if a else i
            case 4, op: b = b ^ c
            case 5, op: R = R + [C[op] & 7]
            case 6, op: b = a >> C[op]
            case 7, op: c = a >> C[op]
        i += 2
    return R



print("part1:", *eval(a,b,c), sep=',')



def find(a, i):
    if eval(a, b, c) == prog: print(a)
    if eval(a, b, c) == prog[-i:] or not i:
        for n in range(8): find(8*a+n, i+1)

def find2(a, i):
    if exec(a) == prog: print(a)
    if exec(a) == prog[-i:] or not i:
        for n in range(8): find(8*a+n, i+1)


find(0, 0)
find2(0, 0)

program = [2,4,1,7,7,5,0,3,4,4,1,7,5,5,3,0]
print(exec(267265166222235))