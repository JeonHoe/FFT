import numpy as np
import matplotlib.pylab as plt

w = np.arange(-2 * np.pi, 2 * np.pi, 0.1) # -2π부터 2π까지 0.1 단위
N = len(w)
Xw = np.zeros(N)
T = 1
for i in range(-int(N/2), int(N/2)):
    if i == 0:
        Xw[i+int(N/2)] = 1
    else:
        Xw[i+int(N/2)] = np.sin(i*T/2)/(i/2)

plt.plot(w,Xw,'blue')
plt.stem(w, Xw,'red')
plt.grid()
plt.show()
