import numpy as np
import matplotlib.pylab as plt

t = np.arange(-2,2,0.01)
f = 0.25; k = 1

w = 2  * np.pi * f

xt1 = np.cos(w * t)
xt2 = np.cos((w + 2 * k * np.pi) * t)

Ts = 2
ohm = w * Ts

n = np.arange(-2,2+Ts,Ts)

xn1 = np.cos(w * n)
xn2 = np.cos((w + 2 * k * np.pi) * n)

plt.subplot(2,1,1); plt.plot(t,xt1,'r'); plt.plot(t,xt2,'b'); plt.grid()
plt.subplot(2,1,2); plt.stem(n,xn1,'r'); plt.stem(n,xn2,'b','.'); plt.grid()
plt.show()