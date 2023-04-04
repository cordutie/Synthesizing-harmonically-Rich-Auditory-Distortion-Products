from functions import *

#Newton method is implemented in the function newton. Its arguments are:
#X=initial condition
#T=target
#e=accepted error
#tolerance=amount of iterations until exit
def newton(X,T,error,tolerance):
    #succes=1 means we won
    #exit=1 means it is time to leave
    exit=0
    iteration=0
    while exit==0:
        while np.dot(F(X,T),F(X,T))>error:
            iteration=iteration+1
            X=np.linalg.solve(DF(X),np.matmul(DF(X),X) - F(X,T))
            if np.dot(F(X,T),F(X,T))<error:
                succes=1
                exit=1
            elif iteration==tolerance:
                succes=0
                exit = 1
    return [succes,X,iteration]

# #Testing
# X=np.array([0.5,0.5,0.5])
# T=np.array([1,2,1])
# error=0.001
# tolerance=100
#
# solucion=newton(T,X,error,tolerance)
# print(T)
#
# print(solucion)
# Y=solucion[1]
# test=np.dot(F(Y,T),F(Y,T))
#
# print("el error final fue de "+ str(test))

