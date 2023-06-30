import numpy as np
import matplotlib.pylab as plt
from chap04.chap04_module import *

xn = [0,1,2,3]; print("x(n)=",xn)
N = len(xn)
Xk = DTFS(xn,N); print("X(k)=",Xk); print("|X(k)|=",np.abs(Xk))

n=np.arange(N)
plt.subplot(2,1,1); plt.stem(n, xn,'blue'); plt.ylabel("x(n)")
plt.grid(); plt.title("DTFS of a discrete periodic signal x(n)")
plt.subplot(2,1,2); plt.stem(n, np.abs(Xk),'green'); plt.xlabel("k"); plt.ylabel("X(k)")
plt.grid()
plt.show()