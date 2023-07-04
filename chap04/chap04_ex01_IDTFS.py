import numpy as np
import matplotlib.pylab as plt
from chap04_module import *

xn = [0,1,2,3] # 이산주기신호의 기본주기구간
N = len(xn) # 이산주기신호의 주기
Xk = DTFS(xn,N); print("|X(k)|=",np.abs(Xk)) # DTFS 계수
ixn = IDTFS(Xk,N); print("x[n]=",ixn) #IDTFS

n=np.arange(N) # 순서시퀀스 생성성
plt.subplot(2,1,1); plt.stem(n, np.abs(Xk),'blue'); plt.ylabel("|X(k)|")
plt.grid(); plt.title("IDTFS of DTFS codfficients X(k)")
plt.subplot(2,1,2); plt.stem(n, ixn,'green'); plt.xlabel("k"); plt.ylabel("x[n]")
plt.grid()
plt.show()