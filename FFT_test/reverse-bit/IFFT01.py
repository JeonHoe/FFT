import numpy as np
import matplotlib.pylab as plt
from test_module import *

# 예시 이산시간 비주기신호 x[n]
xn=[0,1,2,3,4,5]; N=len(xn); print("xn=",xn)

# x[n]의 이산 푸리에 변환
Xk=DFT(xn,N); magXk=np.abs(Xk); print("Magnitude of Xk=",magXk)

# x[n]의 영역 확장 => x1[n]
step=np.log2(N)
if(step-int(step)!=0):
    step=int(step)+1
    N1=np.power(2,step)
    x1n=np.zeros(N1)
    x1n[0:N]=xn; print("x1[n]=",x1n)
else : x1n=np.copy(xn); N1=N; step=int(step)

# 영역 확장된 x[n]의 이산 푸리에 변환
X1k=DFT(x1n,N1); magX1k=np.abs(X1k); print("X1(k)=",X1k); #print("Magnitude of X1k=",magX1k)

# 고속 푸리에 변환(?)
X2k=FFT(xn,N); magX2k=np.abs(X2k); print("X2(k)=",X2k); #print("Magnitude of X2k=",magX2k)

X3k=np.fft.fft(x1n,N1); magX3k=np.abs(X3k); print("X3k=",X3k)
phaX3k=np.angle(X3k,deg=True)


# 역 푸리에 변환 회전인자
WN=np.exp(1j*(2*np.pi/N1))
k=np.arange(N1/2)
WNk=np.power(WN,k)

# X(k)의 reverse bit
print("X2(k)=",X2k)
Xr2k=np.copy(X2k)
for k in range(N1):
    m=0
    for i in range(step):
        m=m|((k>>i)&1)<<(step-i-1)
    if(m>k):
        tmp=Xr2k[k]
        Xr2k[k]=Xr2k[m]
        Xr2k[m]=tmp

print("X'2(k)=",Xr2k) 
magXr1k=np.abs(Xr2k); #print("Magnitude of Reversed bit X2k=",magX2k)

# x[n] 복원
xrn=Xr2k
for loop in range(step):
    regionSize=1<<(loop+1) # N=8:2->4->8
    kjump=1<<(step-loop-1) # N=8:4->2->1
    half=regionSize>>1     # N=8:1->2->4
    for i in range(0,N1,regionSize):
        blockEnd=i+half-1
        k=0
        for j in range(i,blockEnd+1):
            T=WNk[k]*xrn[j+half]
            xrn[j+half]=xrn[j]-T
            xrn[j]=xrn[j]+T
            k+=kjump
xrn=xrn/N1
print("xr(n)=",xrn)

xrrn=np.fft.ifft(X3k,N1)
print("x(n)=",xrrn)

plt.figure(1)
n=np.arange(N)
plt.subplot(2,1,1)
plt.stem(n,xn,'b'); plt.title("x[n] & X(k) DFT"); plt.ylabel("x[n]"); plt.grid()
plt.subplot(2,1,2)
plt.stem(n,Xk,'b'); plt.ylabel("|X(k)|"); plt.grid()

plt.figure(2)
n1=np.arange(N1)
plt.subplot(2,1,1)
plt.stem(n1,x1n,'b'); plt.title("x1[n] & X1(k) DFT"); plt.ylabel("x1[n]"); plt.grid()
plt.subplot(2,1,2)
plt.stem(n1,X1k,'b'); plt.ylabel("|X1(k)|"); plt.grid()

plt.figure(3)
plt.subplot(2,1,1)
plt.stem(n1,x1n,'b'); plt.title("x1[n] & X2(k) FFT version1"); plt.ylabel("x1[n]"); plt.grid()
plt.subplot(2,1,2)
plt.stem(n1,X2k,'b'); plt.ylabel("|X2(k)|"); plt.grid()

plt.figure(4)
plt.subplot(2,1,1)
plt.stem(n1,x1n,'b'); plt.title("x1[n] & X3(k) FFT version2"); plt.ylabel("x1[n]"); plt.grid()
plt.subplot(2,1,2)
plt.stem(n1,X3k,'b'); plt.ylabel("|X3(k)|"); plt.grid()

plt.figure(5)
plt.subplot(2,1,1)
plt.stem(n1,magX2k,'b'); plt.ylabel("|X2(k)|"); plt.grid(); plt.title("Reconstructed of x[n] version1")
plt.subplot(2,1,2)
plt.stem(n1,xrn,'b'); plt.ylabel("xr1[n]"); plt.grid()

plt.figure(6)
plt.subplot(2,1,1)
plt.stem(n1,magX2k,'b'); plt.ylabel("|X2(k)|"); plt.grid(); plt.title("Reconstructed of x[n] version2")
plt.subplot(2,1,2)
plt.stem(n1,xrrn,'b'); plt.ylabel("xr2[n]"); plt.grid()
plt.show()