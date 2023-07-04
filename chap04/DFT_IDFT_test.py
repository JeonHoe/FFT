import numpy as np
import matplotlib.pylab as plt
from chap04_module import *

xn=[1,1,1,1]; print("xn=",xn)
N=len(xn)
n=np.arange(N)

plt.figure(1)
plt.stem(n,xn,'b');plt.xlabel("n");plt.ylabel("x(n)")

Xk=DFT(xn,N); print("Xk=",Xk)
magXk=np.abs(Xk); print("Magnitude of Xk=",magXk)
phaXk=np.angle(Xk,deg=True)
print("Phase of Xk=",phaXk)

plt.figure(2)
plt.subplot(2,1,1); plt.stem(n,magXk,'b');plt.xlabel("k");plt.ylabel("|x(k)|")
plt.subplot(2,1,2); plt.stem(n,phaXk,'b');plt.xlabel("k");plt.ylabel("∠x(k)")

xn=np.real(IDFT(Xk,N)); print("Reconstructed xn=",xn)

plt.figure(3)
plt.stem(n,xn,'b');plt.xlabel("k");plt.ylabel("x(n)")

plt.show()