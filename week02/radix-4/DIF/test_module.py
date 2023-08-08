import numpy as np
import matplotlib.pylab as plt

def DFT(xn, N): # 이산푸리에변환
    WN = np.exp(-1j*(2*np.pi/N)) # 회전인자 계산
    Xk = np.zeros(N,dtype="complex64") # DFT 계수 어레이 설정
    for i in range(N):
        sum = 0
        for j in range(N):
            sum = sum+xn[j]*np.power(WN,i*j) # 개별 DTFS 계수 계산
        Xk[i] = sum
    return Xk

def IDFT(Xk, N): # 역이산푸리에변환
    WN = np.exp(-1j*(2*np.pi/N))
    xn = np.zeros(N,dtype="complex64")
    for i in range(N):
        sum = 0
        for j in range(N):
            sum = sum + Xk[j]*np.power(WN,-i*j)
        xn[i] = sum/N
    return xn

def radix2(x):
    N=len(x)
    if(N==1) : return
    N1=N>>1
    WN=np.exp(-1j*2*np.pi/N)
    y=np.zeros((N1),dtype="complex64")
    z=np.zeros((N1),dtype="complex64")

    for n in range(N1):
        y[n]=x[n]+x[n+N1]
        z[n]=(x[n]-x[n+N1])*np.power(WN,n)
    
    radix2(y); radix2(z)

    for r in range(N1):
        x[r]=y[r]
        x[r+N1]=z[r]
    
def radix4(x):
    N=len(x)
    if(N==1) : return
    elif(N==2) : radix2(x)
    else :
        N1=N>>2
        WN=np.exp(-1j*2*np.pi/N)
        x0=np.zeros((N1),dtype="complex64")
        x1=np.zeros((N1),dtype="complex64")
        x2=np.zeros((N1),dtype="complex64")
        x3=np.zeros((N1),dtype="complex64")

        for n in range(N1):
            x0[n]=x[n]+x[n+N1]+x[n+N1*2]+x[n+N1*3]
            x1[n]=(x[n]-1j*x[n+N1]-x[n+N1*2]+1j*x[n+N1*3])*np.power(WN,n)
            x2[n]=(x[n]-x[n+N1]+x[n+N1*2]-x[n+N1*3])*np.power(WN,2*n)
            x3[n]=(x[n]+1j*x[n+N1]-x[n+N1*2]-1j*x[n+N1*3])*np.power(WN,3*n)
    
        radix4(x0); radix4(x1); radix4(x2); radix4(x3)

        for r in range(N1):
            x[4*r]=x0[r]
            x[4*r+1]=x1[r]
            x[4*r+2]=x2[r]
            x[4*r+3]=x3[r]
    
def i_radix2(x):
    N=len(x)
    if(N==1) : return
    N1=N>>1
    WN=np.exp(1j*2*np.pi/N)
    y=np.zeros((N1),dtype="complex64")
    z=np.zeros((N1),dtype="complex64")

    for n in range(N1):
        y[n]=x[n]+x[n+N1]
        z[n]=(x[n]-x[n+N1])*np.power(WN,n)
    
    i_radix2(y); i_radix2(z)

    for r in range(N1):
        x[r]=y[r]
        x[r+N1]=z[r]

def i_radix4(x):
    N=len(x)
    if(N==1) : return
    elif(N==2) : i_radix2(x)
    else:
        N1=N>>2
        WN=np.exp(1j*2*np.pi/N)
        x0=np.zeros((N1),dtype="complex64")
        x1=np.zeros((N1),dtype="complex64")
        x2=np.zeros((N1),dtype="complex64")
        x3=np.zeros((N1),dtype="complex64")

        for n in range(N1):
            x0[n]=x[n]+x[n+N1]+x[n+N1*2]+x[n+N1*3]
            x1[n]=(x[n]+1j*x[n+N1]-x[n+N1*2]-1j*x[n+N1*3])*np.power(WN,n)
            x2[n]=(x[n]-x[n+N1]+x[n+N1*2]-x[n+N1*3])*np.power(WN,2*n)
            x3[n]=(x[n]-1j*x[n+N1]-x[n+N1*2]+1j*x[n+N1*3])*np.power(WN,3*n)
    
        i_radix4(x0); i_radix4(x1); i_radix4(x2); i_radix4(x3)

        for r in range(N1):
            x[4*r]=x0[r]
            x[4*r+1]=x1[r]
            x[4*r+2]=x2[r]
            x[4*r+3]=x3[r]
    
def reverse_bit(x):
    N=len(x)
    step=np.log2(N)
    if(step-int(step)!=0): return
    step=int(step)
    for n in range(N):
        m=0
        for j in range(step):
            m=m|((n>>j)&1)<<(step-j-1)
        if(n<m):
            tmp=x[n]
            x[n]=x[m]
            x[m]=tmp
