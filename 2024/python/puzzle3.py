import re
import aoc_tools as tools

dataFile = "./dades/input3.txt"







def part1(code):
    res =0
    cad= re.findall("mul\(\d+,\d+\)",sample)
    print(cad)
    for x in cad:
      a,b=tools.nums(x)
      res+=a*b
    print(res)

def part2(code):
    res =0
    campute=True
    cad= re.findall("mul\(\d+,\d+\)|don't\(\)|do\(\)",sample)
    print(cad)
    for x in cad:
        if x=="don't()":
            campute=False
        elif x=="do()":
            campute=True
        else:
            if campute:
                a,b=nums(x)
                res+=a*b
    print(res)
   
if __name__ == '__main__':
    #sample = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    sample = tools.readFileAsString(dataFile)
    part1(sample)
    part2(sample)
   