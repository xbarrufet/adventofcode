import math



program = []

def combo(op,regs):
    if op>0 and op<4:
        return op
    elif op == 4:
        return regs[0]
    elif op == 5:
        return regs[1]
    else:
        return regs[2]
        
    
out =[]

def adv(op,regs):
    regs[0]= math.floor(regs[0]/(2**combo(op,regs)))
    regs[4]+=2
    return regs

def bxl(op,regs):
    regs[1] = regs[1] ^ op
    regs[4]+=2
    return regs

def bst(op,regs):
    regs[1] = combo(op,regs)%8
    regs[4]+=2
    return regs

def jnz(op,regs):
    if regs[0] != 0:
        regs[4]=op
    else:
        regs[4]+=2
    return regs

def bxc(op,regs):
    regs[2] =  regs[2] ^ regs[1]
    regs[4]+=2
    return regs

def out(op,regs):
     regs[3].append(combo(op,regs)%8)
     regs[4]+=2
     return regs

def bdv(op,regs):
    regs[1]= math.floor(regs[0]/(combo(op,regs)*combo(op,regs)))
    regs[4]+=2
    return regs

def cdv(op,regs):
     regs[2]= math.floor(regs[0]/(combo(op,regs)*combo(op,regs)))
     regs[4]+=2
     return regs

INSTRUCTION_SET = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

def run(regs,prgram):
    while regs[4]<len(program):
        ins=program[regs[4]]
        op=program[regs[4]+1]
        regs = INSTRUCTION_SET[ins](op,regs)


if __name__ == '__main__':
    regs = [0,0,9,[],0]
    program=[2,6]
    run(regs,program)
    print(regs)
    
    regs = [10,0,0,[],0]
    program=[5,0,5,1,5,4]
    run(regs,program)
    print(regs)
    
    regs = [2024,0,9,[],0]
    program=[0,1,5,4,3,0]
    run(regs,program)
    print(regs)
    
    regs = [0,29,9,[],0]
    program=[1,7]
    run(regs,program)
    print(regs)
    
    regs = [0,2024,43690,[],0]
    program=[4,0]
    run(regs,program)
    print(regs)
    
    regs = [729,0,0,[],0]
    program=[0,1,5,4,3,0]
    run(regs,program)
    print(regs)
    
    regs = [52042868,0,0,[],0]
    program=[2,4,1,7,7,5,0,3,4,4,1,7,5,5,3,0]
    run(regs,program)
    print(regs)
    
    
    