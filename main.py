from sympy import *
from functions import *
from random import random

#n is the number of equations

def tester(n):
     #Creación de algunos vectores útiles
     canonical_vector=[[] for i in range(n)]
     for i in range(n):
          for j in range(n):
               canonical_vector[i].append(1 if i==j else 0)
     uno = [1 for i in range(n)]
     cero = [0 for i in range(n)]

     #Creation of variables and vector of all variables
     X = [symbols('x%d' % i) for i in range(n)]
     Y = [symbols('y%d' % i) for i in range(n)]
     Variables = X+Y
     init_printing(use_unicode=False, wrap_line=False)

     #Creation of the n equations
     equations=[]
     for i in range(n-1):
          equations.append(inner_prod(X,left_shift_n(X,i+1)))
     equations.append(X[0])
     Y.reverse()
     equations=substraction(equations,Y)

     #SOL=Groebner basis
     SOL=groebner(equations, Variables, domain='QQ', order='lex')

     #LMSOL=set of leading monomials of the polynomials in SOL
     LMSOL=[]
     for i in range(len(SOL)):
          LMSOL.append(polys.polytools.LM(SOL[i], order="lex"))

     #HILBERT_TESTER=set of monomials in LMSOL that have only terms in Y
     HILBERT_TESTER=[]
     for i in range(len(LMSOL)):
          if substitution(LMSOL[i],X,cero)==LMSOL[i]:
               HILBERT_TESTER.append(LMSOL[i])

     #LMSOL_NO_Y=set of monomials in LMSOL evaluated in Y=(1,1,1,...)
     LMSOL_NO_Y=[]
     for i in range(len(LMSOL)):
          LMSOL_NO_Y.append(substitution(LMSOL[i],Y,uno))

     #GROEBNER_TESTER=set of monomials of the form xj^k where every indeterminate is represented just once
     GROEBNER_TESTER=[]
     for i in range(n):
          temp_list=[]
          for j in range(len(LMSOL_NO_Y)):
               if substitution(LMSOL_NO_Y[j],X,canonical_vector[i])==1:
                    temp_list.append(LMSOL_NO_Y[j])
          if len(temp_list)!=0:
               GROEBNER_TESTER.append(temp_list[0])
     Resultados=""
     #Groebner/Hilbert test is used
     if len(HILBERT_TESTER)!=0:
          Resultados+="The system doesn't have solutions when one of the following equations is not null\n"
          for i in range(len(HILBERT_TESTER)):
               Resultados+=str(HILBERT_TESTER[i])+"\n"
          if len(GROEBNER_TESTER) < n:
               Resultados += "If none of the above equations is null, then there are infinite solutions since 1 is not in the ideal and there is at least one indeterminate that doesn't appear in the form xj^k in the groebner basis."
          else:
               Resultados += "If none of the above equations is null, then there are finite solutions since 1 is not in the ideal and the next monomials appear in the Groebner basis:\n"
               for i in range(len(GROEBNER_TESTER)):
                    Resultados += str(GROEBNER_TESTER[i]) + "\n"
          Resultados+="If none of the above equations is satisfied"
     elif len(GROEBNER_TESTER)<n:
          Resultados+="There are infinite solutions since 1 is not in the ideal and there is at least one indeterminate that doesn't appear in the form xj^k in the groebner basis."
     else:
          Resultados+="There are finite solutions since 1 is not in the ideal and the next monomials appear in the Groebner basis:\n"
          for i in range(len(GROEBNER_TESTER)):
               Resultados += str(GROEBNER_TESTER[i]) + "\n"
     return Resultados

for i in range(1,12):
     log_file = open("Test for "+str(i)+" equations.txt", "w")
     log_file.write(tester(i))
     log_file.close()










