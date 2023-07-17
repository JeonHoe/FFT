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

def FFT(xn,N):
    # 영역 확장
    step=np.log2(N)
    if(step-int(step)!=0):
        step=int(step)+1
        N1=np.power(2,step)
        xn1=np.zeros(N1)
        xn1[0:N]=xn
    else: N1=N; xn1=np.copy(xn); step=int(step)

    # 회전인자 
    WN=np.exp(-1j*(2*np.pi/N1))
    k=np.arange(N1/2)
    WNk =np.power(WN,k)

    for n in range(N1):
        m=0
        for j in range(step):
            m=m|((n>>j)&1)<<(step-j-1)
        if(n<m):
            tmp=xn1[n]
            xn1[n]=xn1[m]
            xn1[m]=tmp

    # 계수 계산
    Xk=np.zeros(N1,dtype="complex64") + xn1
    for loop in range(step):
        regionSize=1<<(loop+1) # N=8:2->4->8
        kjump=1<<(step-loop-1) # N=8:4->2->1
        half=regionSize>>1   # N=8:1->2->4
        for i in range(0,N1,regionSize):
            blockEnd=i+half-1
            k=0
            for j in range(i,blockEnd+1):
                T=WNk[k]*Xk[j+half]
                Xk[j+half]=Xk[j]-T
                Xk[j]=Xk[j]+T
                k+=kjump
    return Xk

def IFFT(Xk):
    N=len(Xk)
    step=int(np.log2(N))

    WN=np.exp(1j*(2*np.pi/N))
    k=np.arange(N/2)
    WNk =np.power(WN,k)

    # reverse bit
    Xk1=np.copy(Xk)
    for n in range(N):
        m=0
        for j in range(step):
            m=m|((n>>j)&1)<<(step-j-1)
        if(n<m):
            tmp=Xk1[n]
            Xk1[n]=Xk1[m]
            Xk1[m]=tmp

    # 복원
    xn=np.zeros(N,dtype="complex64")+Xk1
    for loop in range(step):
        regionSize=1<<(loop+1) # N=8:2->4->8
        kjump=1<<(step-loop-1) # N=8:4->2->1
        half=regionSize>>1   # N=8:1->2->4
        for i in range(0,N,regionSize):
            blockEnd=i+half-1
            k=0
            for j in range(i,blockEnd+1):
                T=WNk[k]*xn[j+half]
                xn[j+half]=xn[j]-T
                xn[j]=xn[j]+T
                k+=kjump
    return xn
