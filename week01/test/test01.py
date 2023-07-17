import numpy as np
import matplotlib.pylab as plt

t = np.arange(-1, 1, 0.0001)
print(len(t))
xt1 = np.cos(10 * np.pi * t)
xt2 = np.cos(50 * np.pi * t)

#Fs = 20; Ts = 1 / Fs
Ts = 0.25

n = np.arange(-1, 1 + Ts, Ts)

xn1 = np.cos(10 * np.pi * n)
xn2 = np.cos(50 * np.pi * n)


plt.subplot(3,1,1)
plt.plot(t, xt1, 'b'); plt.plot(t, xt2, 'g'); plt.grid()
plt.subplot(3,1,2)
plt.plot(t, xt1, 'b'); plt.stem(n, xn1, 'r'); plt.grid()
plt.subplot(3,1,3)
plt.plot(t, xt2, 'b'); plt.stem(n, xn2, 'r'); plt.grid()
plt.yticks([-2,-1,0,1,2])
plt.show()