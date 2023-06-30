import numpy as np

def DTFS(xn, N):
    WN = np.exp(-1j*(2*np.pi/N))
    Xk = np.zeros(N,dtype="complex64")
    for i in range(N):
        sum = 0
        for j in range(N):
            sum = sum+xn[j]*np.power(WN,i*j)
        Xk[i] = sum
    return Xk
