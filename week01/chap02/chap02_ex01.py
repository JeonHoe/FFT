import numpy as np
import matplotlib.pyplot as plt

fs = 100; dt = 1/fs; N = 300
t = np.arange(0, N) * dt

# print(t)

x1t = 1.0*np.sin(2*np.pi*1*t)
x2t = 1/3*np.sin(2*np.pi*3*t)
x3t = 1/5*np.sin(2*np.pi*5*t)
xt = x1t + x2t + x3t

df = fs/N
f = np.arange(0, N) * df
Xf = np.fft.fft(xt)

plt.subplot(5,1,1); plt.plot(t,xt,'b'); plt.ylim(-1,1); plt.grid(); plt.ylabel("x(t)")
plt.subplot(5,1,2); plt.plot(t,x1t,'b'); plt.ylim(-1,1); plt.grid(); plt.ylabel("x1(t)")
plt.subplot(5,1,3); plt.plot(t,x2t,'b'); plt.ylim(-1,1); plt.grid(); plt.ylabel("x2(t)")
plt.subplot(5,1,4); plt.plot(t,x3t,'b'); plt.ylim(-1,1); plt.grid(); plt.ylabel("x3(t)")
plt.subplot(5,1,5); plt.plot(f[0:int(N/2+1)],np.abs(Xf[0:int(N/2+1)]),'b')
plt.xlabel("frequency(Hz)"); plt.ylabel("SpectrumX(f)"); plt.grid()
plt.show()