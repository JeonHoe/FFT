import numpy as np
import matplotlib.pylab as plt
from chap04_module import *

N=500
n=np.arange(-4,7)
xn=np.array([0,0,0,1,2,3,4,5,0,0,0])

Omega=np.arange(-2*N,2*N)*2*np.pi/N
X=np.exp(1j*Omega)+2+3*np.exp(-1j*Omega)+4*np.exp(-1j*2*Omega)+5*np.exp(-1j*3*Omega)
magX=np.abs(X)

Omega1=np.arange(0,N)*2*np.pi/N
X1=np.exp(1j*Omega1)+2+3*np.exp(-1j*Omega1)+4*np.exp(-1j*2*Omega1)+5*np.exp(-1j*3*Omega1)
magX1=np.abs(X1)

plt.subplot(3,1,1); plt.stem(n,xn,'b'); plt.grid()
plt.ylabel("x(n)"); plt.title("x(n) & X(Omega), DTFT of x(n)")
plt.subplot(3,1,2); plt.plot(Omega,magX,'b'); plt.xlim(-4*np.pi,4*np.pi); plt.grid(); plt.ylabel("|X(Omega)|")
plt.subplot(3,1,3); plt.plot(Omega1,magX1,'b'); plt.grid()
plt.ylabel('|X(Omega)|'); plt.xlabel("Omega, fruquency in radians"); plt.xlim(0,np.pi)
plt.show()