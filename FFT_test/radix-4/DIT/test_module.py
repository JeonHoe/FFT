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

def radix4(x):
    N=len(x)
    if(N==1) : return

    elif(N==2) :
        radix2(x)
    else :
        a=np.zeros((N>>2),dtype="complex64")
        b=np.zeros((N>>2),dtype="complex64")
        c=np.zeros((N>>2),dtype="complex64")
        d=np.zeros((N>>2),dtype="complex64")

        for i in range(N):
            if(i%4==0): a[i>>2]=x[i]
            elif(i%4==1) : b[i>>2]=x[i]
            elif(i%4==2) : c[i>>2]=x[i]
            elif(i%4==3) : d[i>>2]=x[i]

        radix4(a); radix4(b); radix4(c); radix4(d)

        for k in range(0,(N>>2)):
            Wk1=np.exp(-1j*2*np.pi*k/N); Wk2=np.exp(-1j*2*np.pi*k*2/N); Wk3=np.exp(-1j*2*np.pi*k*3/N)
            x[k]=a[k]+Wk1*b[k]+Wk2*c[k]+Wk3*d[k]
            x[k+(N>>2)]=a[k]-1j*b[k]*Wk1-c[k]*Wk2+1j*d[k]*Wk3
            x[k+(N>>2)*2]=a[k]-b[k]*Wk1+c[k]*Wk2-d[k]*Wk3
            x[k+(N>>2)*3]=a[k]+1j*b[k]*Wk1-c[k]*Wk2-1j*d[k]*Wk3

def i_radix4(x):
    N=len(x)
    if(N==1) : return

    elif(N==2) :
        i_radix2(x)
    else :
        a=np.zeros((N>>2),dtype="complex64")
        b=np.zeros((N>>2),dtype="complex64")
        c=np.zeros((N>>2),dtype="complex64")
        d=np.zeros((N>>2),dtype="complex64")

        for i in range(N):
            if(i%4==0): a[i>>2]=x[i]
            elif(i%4==1) : b[i>>2]=x[i]
            elif(i%4==2) : c[i>>2]=x[i]
            elif(i%4==3) : d[i>>2]=x[i]

        i_radix4(a); i_radix4(b); i_radix4(c); i_radix4(d)

        for k in range(0,(N>>2)):
            Wk1=np.exp(1j*2*np.pi*k/N); Wk2=np.exp(1j*2*np.pi*k*2/N); Wk3=np.exp(1j*2*np.pi*k*3/N)
            x[k]=a[k]+Wk1*b[k]+Wk2*c[k]+Wk3*d[k]
            x[k+(N>>2)]=a[k]-1j*b[k]*Wk1-c[k]*Wk2+1j*d[k]*Wk3
            x[k+(N>>2)*2]=a[k]-b[k]*Wk1+c[k]*Wk2-d[k]*Wk3
            x[k+(N>>2)*3]=a[k]+1j*b[k]*Wk1-c[k]*Wk2-1j*d[k]*Wk3