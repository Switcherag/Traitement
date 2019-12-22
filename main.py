import numpy as np
import matplotlib.pyplt as plt
from mpl_toolkits.mplot3d import Axes3D

#1)______________________Acces aux données_____________________________#
def recup_données(nom)
  donnees = np.loadtxt(nom)  # doonnes c'est une matrice
  global Ax=[];Ay=[];Az=[];Rx=[];Ry=[];Rz=[];  # MAtrice des mesures de l'accelerometre
  M = []  #....

  for ligne in doonnees:
  
    if ligne[0] == 1:
      Ax += [[ligne[2], ligne[1]]]
      Ay += [[ligne[3], ligne[1]]]
      Az += [[ligne[4], ligne[1]]]
      Rx += [[ligne[5], ligne[1]]]
      Ry += [[ligne[6], ligne[1]]]
      Rz += [[ligne[7], ligne[1]]]    
    
    if ligne[0] == 2:
      M += [[ligne[2], ligne[1]]]
  

#2)___________________Exploitation_des_données_accéléromètre_________#

    #a)Trouver  

h = 1e-3  # Pas d'intégration
N = len(Ax)   # Nb de valeurs

v0x = ; v0y= , v0z =  # CI

Vx = [V0x]  # Liste des composantes de vitesse selon ex, ey et ez
Vy = [v0y]
Vz = [v0z]

for i in range(N): # MEP du Schéma RK2
  k1 = Ax[i][0]
  k2 = Ax[i+1][0]
  Vx.append(Vx[-1] + h/2*(k1 + k2)) # Evaluation de d/dt en pt milieux
  Vy.append(Vy[-1] + h/2*(Ay[i][0] + Ay[i+1][0])) # Même principe
  Vz.append(Vz[-1] + h/2*(Az[i][0] + Az[i+1][0]))

x0 = ; y0 = ; z0 =  # CI en position

X = [x0]  # Liste des componsantes de position selon ex, ey et ez
Y = [y0]
Z = [z0]

for i in range(N):
  # On calcule les composantes selon x, y et z, par le même principe de RK2, mtn qu'on a toutes les vitesses
  X.append(X[-1] + h/2*(Vx[i] + Vx[i+1])
  Y.append(Y[-1] + h/2*(Vy[i] + Vy[i+1])
  Z.append(Z[-1] + h/2*(Vz[i] + Vz[i+1])

# Tracé

fig = plt.figure()
X = np.array(X)
Y = np.array(Y)
Z = np.array(Z)

Axes3D.plot(X, Y, Z, color='k')
plt.title('Trajectoire')
plt.xlabel(' X ')
plt.ylabel(' Y ')
plt.show()







