import numpy as np
import matplotlib.pylab as plt
from test_module import *

xn=[1,2,3,4,5]; N=len(xn); print("xn=",xn)

step=np.log2(N)
if(step-int(step)!=0):
    step=int(step)+1
N1=np.power(2,step)
xn1=np.zeros(N1)
xn1[0:N]=xn
xn1[0:N]=xn
print("xn1=",xn1)

WN=np.exp(-1j*(2*np.pi/N1))
k=np.arange(N1/2)
WNk=np.power(WN,k)
PhaWNk=np.angle(WNk,deg=True)
print("PhaWNk=",PhaWNk)

Xk=DFT(xn,N); magXk=np.abs(Xk); print("Magnitude of Xk=",magXk)
n=np.arange(N)
plt.figure(1)
plt.subplot(2,1,1); plt.stem(n,xn,'b'); plt.grid()
plt.subplot(2,1,2); plt.stem(n,magXk,'b'); plt.grid()

Xk1=DFT(xn1,N1); magXk1=np.abs(Xk1); print("Magnitude of Xk=",magXk1)
n1=np.arange(N1)
plt.figure(2)
plt.subplot(2,1,1); plt.stem(n1,xn1,'b'); plt.grid()
plt.subplot(2,1,2); plt.stem(n1,magXk1,'b'); plt.grid(); plt.show()