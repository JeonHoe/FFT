import numpy as np
import matplotlib.pylab as plt
from chap03_module import *

n1=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
x1=np.array([0,0,0,1,2,3,4,5,6,7,6,5,4,3,2,1])
n2=np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7])
x2=np.array([1,2,3,4,5,6,7,6,5,4,3,2,1])

# 신호덧셈
n,y,zx1,zx2=sigadd(n1,x1,n2,x2); print("y(n)=",y)
print('x1(n)=',zx1); print('x2(n)=',zx2); print('n=',n)
plt.figure(1)
plt.subplot(3,1,1); plt.stem(n,zx1,'b'); plt.grid()
plt.ylabel('x1(zx1)'); plt.title("Signal Addition")
plt.subplot(3,1,2); plt.stem(n,zx2,'b'); plt.grid(); plt.ylabel('x2(zx2)')
plt.subplot(3,1,3); plt.stem(n,y,'b'); plt.grid(); plt.xlabel("n"); plt.ylabel("y=x1+x2")
plt.show()

# 신호곱셈
n,y,zx1,zx2=sigmult(n1,x1,n2,x2); print("y(n)=",y)
print('x1(n)=',zx1); print('x2(n)=',zx2); print('n=',n)
plt.figure(2)
plt.subplot(3,1,1); plt.stem(n,zx1,'b'); plt.grid()
plt.ylabel('x1(zx1)'); plt.title("Signal Multiplication")
plt.subplot(3,1,2); plt.stem(n,zx2,'b'); plt.grid(); plt.ylabel('x2(zx2)')
plt.subplot(3,1,3); plt.stem(n,y,'b'); plt.grid(); plt.xlabel("n"); plt.ylabel("y=zx1*zx2")
plt.show()

# 신호크기조정
x1=np.array([0,0,0,1,2,3,4,5,6,7,6,5,4,3,2,1]); print("x1(n)=",x1)
y=3*x1; print("y(n)=3*x1(n)=",y)
plt.figure(3)
plt.subplot(2,1,1); plt.stem(n1,x1,'b'); plt.grid(); plt.ylim(0,22)
plt.ylabel("x1(n)"); plt.title("Signal Scaling")
plt.subplot(2,1,2); plt.stem(n1,y,'b'); plt.grid(); plt.ylim(0,22)
plt.xlabel('n'); plt.ylabel('y(n)=3*x1(n)')
plt.show()

# 신호이동
k=4
n,y=sigshift(n1,x1,k); print('n=',n); print('y(n)=',y)
plt.figure(4)
plt.subplot(2,1,1); plt.stem(n1,x1,'b'); plt.grid()
plt.ylabel("x1(n)"); plt.title("Signal Shifting")
plt.subplot(2,1,2); plt.stem(n,y,'b'); plt.grid()
plt.xlabel('n'); plt.ylabel('shift k=4, y(n)')
plt.show()