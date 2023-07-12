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
    odd=np.zeros((N>>1),dtype="complex64")
    even=np.zeros((N>>1),dtype="complex64")
    for i in range(N):
        if(i%2==1): odd[i>>1]=x[i]
        else : even[i>>1]=x[i]
    radix2(even); radix2(odd)
    for k in range(0,(N>>1)):
        Wk=np.exp(-1j*2*np.pi*k/N)
        x[k]=even[k]+Wk*odd[k]
        x[k+(N>>1)]=even[k]-Wk*odd[k]

def i_radix2(x):
    N=len(x)
    if(N==1): return
    odd=np.zeros((N>>1),dtype="complex64")
    even=np.zeros((N>>1),dtype="complex64")
    for i in range(N):
        if(i%2==0): even[i>>1]=x[i]
        else : odd[i>>1]=x[i]
    i_radix2(even); i_radix2(odd)
    for k in range(0,(N>>1)):
        Wk=np.exp(1j*2*np.pi*k/N)
        x[k]=even[k]+Wk*odd[k]
        x[k+(N>>1)]=even[k]-Wk*odd[k]