import numpy as np
import matplotlib.pylab as plt

N = 500
n = np.arange(30)
xn = np.power(0.5,n)
Omega = np.arange(-2*N,2*N)*2*np.pi/N
X=np.exp(1j*Omega)/(np.exp(1j*Omega)-0.5)


plt.subplot(2,1,1); plt.stem(n,xn,'b'); plt.grid()
plt.ylabel("x(n)"); plt.title("x(n) & X(Omega), DTFT of x(n)")
plt.subplot(2,1,2); plt.plot(Omega,X); plt.grid()
plt.ylabel('|X(Omega)|'); plt.xlabel("Omega, fruquency in radians")
plt.show()