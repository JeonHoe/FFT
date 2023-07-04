import numpy as np
import matplotlib.pylab as plt
from scipy import interpolate

Ts = 0.0002
n = np.arange(-25,26)
xn = np.exp(-1000*np.abs(n*Ts))

ft=interpolate.interp1d(n,xn,kind='linear')
tn=np.linspace(-25,25,1000)

plt.subplot(2,1,1); plt.stem(n,xn,"blue"); plt.ylabel("x(n)"); plt.grid()
plt.title("Signal reconstruction using zero-order interpolation")
plt.subplot(2,1,2); plt.plot(tn, ft(tn),"red"); plt.grid()
plt.xlabel("tn"); plt.ylabel("xa(t)")
plt.stem(n,xn,"blue",".")
plt.show()
