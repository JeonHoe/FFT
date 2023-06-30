import numpy as np
import matplotlib.pylab as plt

fs = 5000; Ts = 0.0002
n = np.arange(-25, 26)
xn = np.exp(-1000*np.abs(n*Ts))
N = len(n)

dt = 0.000005
t = np.arange(-0.005, 0.005, dt)
Nt = len(t)

sinc_out = np.zeros(Nt)
for i in range(Nt):
    sum = 0
    for j in range(N):
        sum = sum + xn[j] * np.sinc(fs * (i * dt - j * Ts))
        sinc_out[i] = sum

plt.subplot(2,1,1); plt.stem(n,xn,'blue'); plt.ylabel('x[n]'); plt.grid()
plt.title('x[n], Reconstructed signal using sinc function')
plt.subplot(2,1,2); plt.plot(t, sinc_out, 'red')
plt.xlabel("time in msec"); plt.ylabel('x(t)'); plt.grid()
plt.show()