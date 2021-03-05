import numpy as np

hbar = 5.806484171
#Row
F = np.array(        
    [[ 4.877666490402689E+05, -3.402909255277740E+03,  1.260024558228502E+04],
     [-3.402909255277740E+03,  4.877062385099230E+05,  1.247280561832061E+04],
     [ 1.260024558228502E+04,  1.247280561832061E+04,  3.992753726783524E+04]])
#Column
GF = np.array(
    [[ 5.13723E+05, -1.20793E+04,  1.05408E+04],
     [-1.20884E+04,  5.13667E+05,  1.04044E+04],
     [-8.38628E+02, -1.13948E+03,  9.38646E+04]])

VR_1 = np.array(
    [[0.009762,  -7.664145,   7.647219],
     [0.013037,  -7.683767,  -7.627020],
     [4.698844,  -0.394243,   0.002902]])


VR = np.array(
        [[ -0.005501,  -0.065077,   0.065552],
         [ -0.005434,  -0.065250,  -0.065387],
         [  0.212845,   0.000316,   0.000045]])

VR_norm = np.array(
         [[ -0.025826,  -0.706168,   0.707998],
          [ -0.025514,  -0.708036,  -0.706215],
          [  0.999341,   0.003431,   0.000488]])


freq = np.array([1779.4331856231,4112.2053598171,4210.3171790240])

e_val, e_vec = np.linalg.eig(GF)
print(e_val,e_vec)
e_vec[:,[2,0]] = e_vec[:,[0,2]]
VR_new = e_vec.copy()
e_val2 = e_val.copy()
e_val[0] = e_val2[2]
e_val[2] = e_val2[0]
for i in range(3):
    temp = 0
    for j in range(3):
        for k in range(3):
            temp += e_vec.T[i,k] * e_vec.T[i,j] * F[k,j]
    temp = abs(temp)
    temp = np.sqrt(hbar*np.sqrt(abs(e_val[i])) / temp)
    for j in range(3):
        VR_new.T[i,j] *= temp 

print(f'VR_new = \n{VR_new}\n\nVR = \n{VR}\n\n')

VR_inv = np.linalg.inv(VR_new.T)


strang = ''
for i in range(3):
    for j in range(3):
        strang += ' {} '.format(VR_new[i,j] / VR[i,j])
    strang += '\n'
#print(strang)


ar = np.dot(VR.T,np.dot(F,VR))

evals_N = np.zeros((3))
for i in range(3):
    evals_N[i] = ar[i,i]

#print(5.806484171*(e_val**0.5))



