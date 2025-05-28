import sys
from math import log2

operatorsFileName = "operators"
operandsFileName = "operands"
programFileName = "text.txt"

operators = {}
operands = {}

with open(operatorsFileName) as f:
    for op in f:
        operators[op.replace('\n','')] = 0

with open(operandsFileName) as f:
    for op in f:
        operands[op.replace('\n','')] = 0

isAllowed = True

with open(programFileName) as f:
    for line in f:
        line = line.strip("\n").strip(' ')

        if(line.startswith("/*")):
            isAllowed = False
       
        if((not line.startswith("//")) and isAllowed == True and (not line.startswith('#'))):
            for key in operators.keys():
                operators[key] = operators[key] + line.count(key)
                line = line.replace(key,' ')
            for key in operands.keys():
                operands[key] = operands[key] + line.count(key)
                line = line.replace(key,' ')

        if(line.endswith("*/")):
            isAllowed = True


n1, N1, n2, N2 = 0, 0, 0, 0

print("OPERATORS:\n")
for key in operators:
    if(operators[key] > 0):
        if(key not in ")}]SystemnamespacestaticclassargsConsolestringusingmetrickvoidMainint"):
            n1, N1 = n1 + 1, N1 + operators[key]
            if(key in "("):
                print("{} = {}".format(key +")", operators[key]))
            else:
                if(key in "{"):
                    print("{} = {}".format(key +"}", operators[key]))
                else:
                    if(key in "["):
                        print("{} = {}".format(key +"]", operators[key]))
                    else:
                        print("{} = {}".format(key, operators[key]))

print("\n OPERANDS:\n")
for key in operands.keys():
    if(operands[key] > 0):
        n2, N2 = n2 + 1, N2 + operands[key]
        print("{} = {}".format(key, operands[key]))

val = {"1n":n1,"2n":n2,"1N":N1,"2N":N2,"N": N1 + N2, "n": n1 + n2, "V": (N1 + N2) * log2(n1 + n2), "S": n1 * N2 / 2 / n2,"Nt":n1*log2(n1)+n2*log2(n2),"V*":(N1 + N2)*log2(n1 + n2)}
val['E'] = val['S'] * val['V']
val['L'] = val['V'] / val['S'] / val['S']
val['T'] = val['E'] / (10)
val['L*'] = 2 * n2 / N2 / n1
val['I'] = val['V'] * val['L*']
val['T^'] = n1*N2 * (N1+N2)*log2(n1+n2) / (2*10*n2)
val['B'] = val['V'] / 3000
unit = {'V': 'bits', 'T': 'seconds'}
name = {'1n':'The number of different operators','2n':'The number of different operands','1N':'The total number of operators','2N':'The total number of operands','N':'Halstead Program Length', 'n':'Halstead Vocabulary ','Nt':'Length estimation', 'V':'Program Volume','V*':'Potential volume', 'L':'Language level', 'L*':'Estimated language level', 'S':'Program Difficulty', 'E': 'Programming Effort', 'I':'Intellect', 'T':'Programming time','T^':'Time estimation','B':'Error'}
print(" \n The various values are: \n")
for key in val.keys():
    print("{} ({}) = {} {}".format(key,name[key], val[key], unit[key] if key in unit else ''))