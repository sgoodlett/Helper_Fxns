from re import compile, search, match

a = compile(r'^\s*Output of python function: -?\d*.\d*$')

c = 0
d = 0
with open('file.dat','r') as fn:
    for line in fn.readlines():
        d += 1
        if match(a,line):
            c += 1
        
print(c, d)
