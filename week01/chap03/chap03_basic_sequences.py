import numpy as np
import matplotlib.pylab as plt
from chap03_module import *

# 이산신호
n=[-3,-2,-1,0,1,2,3,4] # 순서 시퀀스
xn=[2,1,-1,0,1,4,3,7]  # 샘플 시퀀스
plt.figure(1); plt.stem(n,xn,'b'); plt.grid()
plt.xlabel('n'); plt.ylabel("x(n)")
plt.title("Representation of a sequence x(n)"); plt.show()

# 단위샘플
n0=10; n1=0; n2=20
N=n2-n1+1; n=np.arange(n1,n2+1)
xn=impseq(n0,n1,n2); print('Unit sample sequence=',xn)
plt.figure(2)
plt.stem(n,xn,'b'); plt.grid()
plt.xlabel('n'); plt.ylabel("x(n)")
plt.title("Unit sample sequence"); plt.show()

# 단위계단
n0=10; n1=0; n2=20
N=n2-n1+1; n=np.arange(n1,n2+1)
xn=stepseq(n0,n1,n2); print('Unit step sequence=',xn)
plt.figure(3)
plt.stem(n,xn,'b'); plt.grid()
plt.xlabel('n'); plt.ylabel("x(n)")
plt.title("Unit step sequence"); plt.show()

# 실수지수
a=0.7
N=20; n=np.arange(N)
xn=np.power(a,n); print("Real-Valued exponential=",xn)
plt.figure(4)
plt.stem(n,xn,'b'); plt.grid()
plt.xlabel('n'); plt.ylabel("x(n)")
plt.title("Real-Valued exponential sequence"); plt.show()

# 복소지수
sigma=2; freq=3
n=np.linspace(0,10,100)
xn=np.exp((sigma+freq*1j)*n)
magxn=np.abs(xn)
plt.figure(5)
plt.subplot(2,1,1); plt.stem(n,xn,'b'); plt.grid()
plt.ylabel('x(n), Amplitude')
plt.title("Complex_valued exponential sequence")
plt.subplot(2,1,2); plt.stem(n,magxn,'b'); plt.grid()
plt.xlabel('n'); plt.ylabel('|x(n)|, magnitude'); plt.show()

# 정현파
n=np.linspace(0,10*np.pi,100)
xn=3*np.cos(0.1*np.pi*n+np.pi/2)
plt.figure(6)
plt.stem(n,xn,'b'); plt.grid()
plt.xlabel('n[samples]'); plt.ylabel('Amplitude')
plt.title("Sinusoidal sequence"); plt.show()

# 무작위
n=np.arange(20)
xn=np.random.rand(20); print("Random sequence x(n)=",xn)
plt.figure(7)
plt.stem(n,xn,'b'); plt.grid()
plt.xlabel('n'); plt.ylabel('amplitude')
plt.title('Random sequence'); plt.show()

# 주기
x=[1,2,3,4,5,6,7]; print('x=',x)
xn=5*x; print('xn=',xn)
plt.figure(8)
n=np.arange(35)
plt.stem(n,xn,'b'); plt.grid()
plt.xlabel("n"); plt.ylabel('amplitude')
plt.title("Periodic sequence"); plt.show()