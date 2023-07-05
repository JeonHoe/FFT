import numpy as np
import matplotlib.pylab as plt

N=128
n=np.arange(N)
n1=n[0:int(N/2)]
xn=np.cos(0.48*np.pi*n)+np.cos(0.52*np.pi*n)

Xk=np.fft.fft(xn,N)
magXk=np.abs(Xk)
magXk1=magXk[0:int(N/2)]
xnt=np.fft.ifft(Xk)

plt.figure(1)
plt.subplot(3,1,1); plt.stem(n,xn); plt.grid(); plt.ylabel("Input x[n]")
plt.title("Input sequence x[n], FFT X(k), IFFT xr[n]")
plt.subplot(3,1,2); plt.stem(n1,magXk1,'g'); plt.grid(); plt.ylabel("|X(k)|")
plt.subplot(3,1,3); plt.stem(n,xnt,'g'); plt.ylabel('Reconstructed xr(n)')
plt.xlabel('k'); plt.grid(); plt.show()