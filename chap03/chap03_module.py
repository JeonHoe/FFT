import numpy as np
import matplotlib.pylab as plt

def impseq(n0,n1,n2): # 단위샘플시퀀스
    N=n2-n1+1 # 데이터 수
    n=np.arange(N)
    xn=np.zeros(N)
    for i in range(N):
        if(i+n1 == n0): xn[i] = 1
    return xn

def stepseq(n0,n1,n2):
    N=n2-n1+1
    n=np.arange(N)
    xn=np.zeros(N)
    for i in range(N):
        if(i+n1>=n0): xn[i]=1
    return xn

def sigadd(n1,x1,n2,x2): # 신호덧셈
    nk=np.arange(min(min(n1),min(n2)),max(max(n1),max(n2))+1)
    N=len(nk)
    y1=np.zeros(N)
    y2=np.zeros(N)
    aa=abs(min(min(n1),min(n2)))
    n1=n1+aa; n2=n2+aa
    y1[int(min(n1)):int(max(n1)+1)]=x1
    y2[int(min(n2)):int(max(n2)+1)]=x2
    y=y1+y2
    return nk,y,y1,y2

def sigmult(n1,x1,n2,x2): # 신호곱셈
    nk=np.arange(min(min(n1),min(n2)),max(max(n1),max(n2))+1)
    N=len(nk)
    y1=np.zeros(N)
    y2=np.zeros(N)
    aa=abs(min(min(n1),min(n2)))
    n1=n1+aa; n2=n2+aa
    y1[int(min(n1)):int(max(n1)+1)]=x1
    y2[int(min(n2)):int(max(n2)+1)]=x2
    y=y1.T*y2
    return nk,y,y1,y2

def sigshift(m,x,k): # 신호이동
    n=m+k
    y=x
    return n,y