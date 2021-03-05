from re import compile, match
import math
import numpy as np
from numpy.linalg import norm

tag_line = compile(r'\$([\w()]*):(a[dtq5]z)')
biggun = {}
with open('file.txt','r') as fn:
    for line in fn:
        matches = match(tag_line,line)
        if matches:
            tom_brady = 0
            geom = [[],[],[],[]]
            method, basis = matches.group(1,2)
        
        else:
            pieces = line.split()
            geom[tom_brady] = [float(i) for i in pieces[1:4]]
            tom_brady += 1
            if tom_brady == 3:
                biggun[f'{method}:{basis}'] = geom

nextun = {}

for key in biggun:
    m = biggun[key]
    r1 = (((m[0][0] - m[1][0])**2) + ((m[0][1] - m[1][1])**2) + ((m[0][2] - m[1][2])**2))**(0.5)  #OH length
    r2 = (((m[0][0] - m[2][0])**2) + ((m[0][1] - m[2][1])**2) + ((m[0][2] - m[2][2])**2))**(0.5)  #OO length
    r3 = (((m[0][0] - m[3][0])**2) + ((m[0][1] - m[3][1])**2) + ((m[0][2] - m[3][2])**2))**(0.5)  #OH' length
    a1 = math.acos(((r3**2) - (r1**2) - (r2**2)) / (-2 * r1 *r2)) * (180 / math.pi)
    n1 = np.cross([m[0][0]-m[1][0], m[0][1]-m[1][1], m[0][2]-m[1][2]], [m[0][0]-m[2][0], m[0][1]-m[2][1], m[0][2]-m[2][2]])
    n2 = np.cross([m[2][0]-m[0][0], m[2][1]-m[0][1], m[2][2]-m[0][2]], [m[2][0]-m[3][0], m[2][1]-m[3][1], m[2][2]-m[3][2]])
    d1 = math.acos(np.dot(n1/norm(n1),n2/norm(n2))) * (180/math.pi)
    nextun[key] = [d1]
print(nextun)
