import psi4
import numpy as np

geom = """
0 3
O
O 1 r1
H 1 r2 2 a1
H 2 r3 1 a2 3 d1

r1 = 1.809056191785725
r2 = 1.1
r3 = {0}
a1 = 91.083269531831675
a2 = 91.083269531831675
d1 = 180.000000000000000

"""
#r1 = 1.809056191785725
#r2 = 0.952535318040152 
#a1 = 91.083269531831675
#d1 = 180.000000000000000

arr = np.linspace(0.7, 1.1, 25)
rs = []
es = []
for i in arr:
    #psi4.set_memory('1 gb')
    psi4.core.be_quiet()
    mol = psi4.geometry(geom.format(i))
    psi4.set_options({'e_convergence':8,'scf_type':'pk','reference':'uhf','basis':'aug-cc-pvdz','geom_maxiter':100,'maxiter':500,
                      'optking__max_force_g_convergence':5e-4,'optking__rms_force_g_convergence':5e-4,'optking__max_energy_g_convergence':1e-5,
                      'optking__frozen_bend':('1 2 3')})
    e = psi4.energy('scf', molecule=mol)
    rs.append(i)
    es.append(e*psi4.constants.hartree2kcalmol)
    psi4.core.clean()

strang = '   Param       E (kcal/mol)     \n-------------------------------\n'
print(es)
es = np.array(es)
es -= min(es)

for i in range(len(rs)):
    strang += f'{rs[i]:13.7f}      {es[i]:15.11f} \n'

with open('scan.dat','w') as fn:
    fn.write(strang)
