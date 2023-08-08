import numpy as np
import matplotlib.pylab as plt
from test_module import *

xn=np.arange(64); N=len(xn); print("x[n]=",xn)

Xk=DFT(xn,N); magXk=np.abs(Xk); phaXk=np.angle(Xk,deg=True)
#print("|X(k)|=",magXk)
#print("∠X(k)=",phaXk)

step=np.log2(N)
if(step-int(step)!=0):
    step=int(step)+1
    N1=np.power(2,step)
    x1n=np.zeros(N1)
    x1n[0:N]=xn
else : x1n=np.copy(xn); N1=N; step=int(step)

print("x1[n]=",x1n)

Xk_DFT=DFT(x1n,N1); magXk_DFT=np.abs(Xk_DFT); phaXk_DFT=np.angle(Xk_DFT,deg=True)
print("Xk = ",Xk_DFT)
print("|X(k)| of DFT=",magXk_DFT)
#print("∠X1(k) of DFT=",phaXk_DFT)

Xk=np.zeros(len(x1n),dtype="complex64")+x1n

radix4(Xk)
#sort_radix4(Xk)

print("Xk = ",Xk)
print("|X(k)| of FFT(radix4)=",np.abs(Xk))
#print("∠X(k) of FFT(radix2)=",np.angle(Xk,deg=True))

plt.figure(1)
n1=np.arange(N1)
plt.stem(n1,x1n); plt.title("n1 & x1[n]")
plt.xlabel("n"); plt.ylabel("x[n]"); plt.grid()

plt.figure(2)
plt.subplot(2,1,1) ;plt.stem(n1,x1n); plt.title("x1[n] & X(k) DFT")
plt.ylabel("x[n]"); plt.grid()
plt.subplot(2,1,2) ;plt.stem(n1,magXk_DFT)
plt.ylabel("|X(k)|"); plt.grid()

plt.figure(3)
plt.subplot(2,1,1) ;plt.stem(n1,x1n); plt.title("x1[n] & X(k) FFT (radix-4)")
plt.ylabel("x[n]"); plt.grid()
plt.subplot(2,1,2) ;plt.stem(n1,np.abs(Xk))
plt.ylabel("X(k)"); plt.grid()
plt.show()
