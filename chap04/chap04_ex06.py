import numpy as np
import matplotlib.pylab as plt
from chap04_module import *

N=10
xn=np.zeros(N,dtype='float')
for i in range(N):
    xn[i]=np.cos(i*np.pi*0.48)+np.cos(i*np.pi*0.52)
t=np.arange(0,N,0.0001)
xt=np.cos(t*np.pi*0.48)+np.cos(t*np.pi*0.52)
Xk=DFT(xn,N); magXk=np.abs(Xk)
print("xn=",xn)
print("Magnitude of Xk=",magXk)
n=np.arange(N)
fn=np.linspace(0,np.pi,int(N/2)+1); print("fn=",fn)

plt.figure(1)
plt.subplot(2,1,1); plt.stem(n,xn); plt.plot(t,xt,":"); plt.grid()
plt.subplot(2,1,2); plt.stem(fn,magXk[0:int(N/2)+1]); plt.grid(); plt.show()

N1=100
xn1=np.zeros(N1,dtype='float')
xn1[0:N]=xn; n1=np.arange(N1)
Xk1=DFT(xn1,N1); magXk1=np.abs(Xk1)
fn1=np.linspace(0,np.pi,int(N1/2)+1)
t1=np.arange(0,N1,0.0001)
xt1=np.cos(t1*np.pi*0.48)+np.cos(t1*np.pi*0.52)
plt.figure(2)
plt.subplot(2,1,1); plt.stem(n1,xn1); plt.plot(t1,xt1,":"); plt.grid()
plt.subplot(2,1,2); plt.stem(fn1,magXk1[0:int(N1/2)+1]); plt.grid(); plt.show()

N2=100
xn2=np.zeros(N2,dtype="float")
for i in range(N2):
    xn2[i]=np.cos(i*np.pi*0.48)+np.cos(i*np.pi*0.52)
Xk2=DFT(xn2,N2); magXk2=np.abs(Xk2)
fn2=np.linspace(0,np.pi,int(N2/2)+1)
plt.figure(3)
plt.subplot(2,1,1); plt.stem(n1,xn2); plt.plot(t1,xt1,":"); plt.grid()
plt.subplot(2,1,2); plt.stem(fn2,magXk2[0:int(N2/2)+1]); plt.grid(); plt.show()


