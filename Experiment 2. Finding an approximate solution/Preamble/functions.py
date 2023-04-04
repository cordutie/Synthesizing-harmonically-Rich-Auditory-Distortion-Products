import numpy as np

#S is the left shift function. For example, S(1,2,3)=(2,3,0)
def S(X):
    N=X.size
    shifted=np.zeros(N)
    for i in range(0,N-1):
        shifted[i]=X[i+1]
    return shifted

#R is the right shift function. For example, S(1,2,3)=(0,1,2)
def R(X):
    N=X.size
    shifted=np.zeros(N)
    for i in range(0,N-1):
        shifted[i+1]=X[i]
    return shifted

#SN(X,n) applies S n times to the vector X
def SN(X,n):
    nshifted=X
    for i in range(0,n):
        nshifted=S(nshifted)
    return nshifted

#RN(X,n) applies R n times to the vector X
def RN(X,n):
    nshifted=X
    for i in range(0,n):
        nshifted=R(nshifted)
    return nshifted

#The function A generates the right part of the equation (17) in the paper considering A_1=1. For example,
#A(2,3,4)=( 1*2 + 2*3 + 3*4  =(20
#           1*3 + 2*4          11
#           1*4             )  4)
#A:R^N -> R^N, where N+1 is the number of sinusoids and N is the number of target harmonics.
def A(X):
    N=X.size
    Y=np.zeros(N+1)
    Y[0]=1
    for i in range(1,N+1):
        Y[i]=X[i-1]
    Z=np.zeros(N)
    for i in range(0,N):
        Z[i]=np.dot(Y,SN(Y,i+1))
    return Z

#The function F is the system (17) equals 0 again with A_1=1.
def F(X,T):
    return A(X)-T

#The Jacobian matrix is defined
def DF(X):
    N=X.size
    Z=np.zeros((N,N))
    for i in range(0,N-1):
        temp=SN(X,i+1)+RN(X,i+1)
        for j in range(0,N):
            Z[i,j]=temp[j]
    Z=Z+np.identity(N)
    return Z

#Testing
# a = np.array([2,3,4])
# print(a)





