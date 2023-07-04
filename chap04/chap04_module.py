import numpy as np

def DTFS(xn, N): # 이산주기신호와 주기로부터 DTFS 계수 구하는 함수
    WN = np.exp(-1j*(2*np.pi/N))
    Xk = np.zeros(N,dtype="complex64") # DTFS 계수 어레이 설정
    for i in range(N):
        sum = 0
        for j in range(N):
            sum = sum+xn[j]*np.power(WN,i*j) # 개별 DTFS 계수 계산
        Xk[i] = sum/N
    return Xk

def IDTFS(Xk, N): # DFS 계수 Xk와 주기 N으로부터 시퀀스 x(n)을 구하는 역 DFS
    WN = np.exp(-1j*(2*np.pi/N))
    xn = np.zeros(N,dtype="complex64")
    for i in range(N):
        sum = 0
        for j in range(N):
            sum = sum + Xk[j]*np.power(WN,-i*j)
        xn[i] = sum
    return xn

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

def DTFT(xn, N, T): #이산시간푸리에변환 *단, 교재 p.155에 x[n] 한정에 DTFT
    w=np.linspace(0.001,2*np.pi,T)
    MXe=np.zeros(T,dtype="complex64")
    for i in range(T):
        MXe[i]=np.sin(2*w[i])/np.sin(w[i]/2)*np.exp(-1j*1.5*w[i])
    return MXe