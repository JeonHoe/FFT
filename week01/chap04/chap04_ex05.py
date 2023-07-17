import numpy as np
import matplotlib.pylab as plt
from chap04_module import *

xn = [1,1,1,1]; N=4; print("xn=",xn,"N=",N)
Xk=DFT(xn,N)
magXk=np.abs(Xk); print("Magnitude of Xk=",magXk)

xn1=[1,1,1,1,0,0,0,0]; N1=8; print("xn1=",xn1,"N1=",N1)
Xk1=DFT(xn1,N1)
magXk1=np.abs(Xk1); print("Magnitude of Xk1=",magXk1)

xn2=[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0]; N2=16; print("xn1=",xn2,"N1=",N2)
Xk2=DFT(xn2,N2)
magXk2=np.abs(Xk2); print("Magnitude of Xk2=",magXk2)

nT=1000
MXe=DTFT(xn,N,nT); magMXe=np.abs(MXe)
w=np.linspace(0,np.pi,nT)