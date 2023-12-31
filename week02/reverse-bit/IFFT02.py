import numpy as np
import matplotlib.pylab as plt
from test_module import *

# 예시 이산시간 비주기신호 x[n]
xn=[2,1,4,5,6,8,7,3]; N=len(xn); print("xn=",xn)

# x[n]의 이산 푸리에 변환
Xk=DFT(xn,N); magXk=np.abs(Xk); print("Magnitude of Xk=",magXk)
phaXk=np.angle(Xk,deg=True)

# x[n]의 영역 확장 => x1[n]
step=np.log2(N)
if(step-int(step)!=0):
    step=int(step)+1
    N1=np.power(2,step)
    x1n=np.zeros(N1)
    x1n[0:N]=xn; print("x1[n]=",x1n)
else : x1n=np.copy(xn); N1=N; step=int(step)

# 영역 확장된 x[n]의 이산 푸리에 변환
X1k=DFT(x1n,N1); magX1k=np.abs(X1k); print("Magnitude of X1k=",magX1k)
phaX1k=np.angle(X1k,deg=True)

# 고속 푸리에 변환(?)
X2k=FFT(xn,N); magX2k=np.abs(X2k); print("Magnitude of X2k=",magX2k)
phaX2k=np.angle(X2k,deg=True)

# 역 고속 푸리에 변환(?)
x2n=IFFT(X2k); print("x2(n)=",x2n)

# 역 고속 푸리에 변환
x3n=np.fft.ifft(X2k); print("x3(n)=",x3n)

plt.figure(1)
n=np.arange(N)
plt.subplot(2,1,1)
plt.stem(n,xn,'b'); plt.title("x[n] & X(k) DFT"); plt.ylabel("x[n]"); plt.grid()
plt.subplot(2,1,2)
plt.stem(n,magXk,'b'); plt.ylabel("|X(k)|"); plt.grid()

plt.figure(2)
n1=np.arange(N1)
plt.subplot(2,1,1)
plt.stem(n1,x1n,'b'); plt.title("x1[n] & X1(k) DFT"); plt.ylabel("x1[n]"); plt.grid()
plt.subplot(2,1,2)
plt.stem(n1,magX1k,'b'); plt.ylabel("|X1(k)|"); plt.grid()

plt.figure(3)
plt.subplot(2,1,1)
plt.stem(n1,x1n,'b'); plt.title("x1[n] & X2(k) FFT version1"); plt.ylabel("x1[n]"); plt.grid()
plt.subplot(2,1,2)
plt.stem(n1,magX2k,'b'); plt.ylabel("|X2(k)|"); plt.grid()

plt.figure(4)
plt.subplot(2,1,1)
plt.stem(n1,magX2k,'b'); plt.title("Reconducted of x(n) version1"); plt.ylabel("X2(k)"); plt.grid()
plt.subplot(2,1,2)
plt.stem(n1,x2n,'b'); plt.ylabel("xr1(n)"); plt.xlabel("n"); plt.grid()

plt.figure(5)
plt.subplot(2,1,1)
plt.stem(n1,magX2k,'b'); plt.title("Reconducted of x(n) version2"); plt.ylabel("X2(k)"); plt.grid()
plt.subplot(2,1,2)
plt.stem(n1,x3n,'b'); plt.ylabel("xr2(n)"); plt.grid()
plt.show()
