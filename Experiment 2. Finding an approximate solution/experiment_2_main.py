from Preamble.functions import *
from Preamble.results_building import *
import copy

#Create a list of m targets of n entries
m=10000
n=8
targets=[]
for i in range(m):
    targets.append(np.random.rand(n))

#Try to solve every target up to l times and save the targets that couldn't be solved
l=10
bad_targets=[]
for i in range(len(targets)):
    j=0
    succes=0
    while succes==0 and j<l:
        j+=1
        temp_sol=newton(np.random.rand(n),targets[i],0.0001,100)
        succes=temp_sol[0]
    if succes==0:
        bad_targets.append(targets[i])

print(str(len(bad_targets))+" bad targets were found")

#If no solution could be found, try with T + a small random vector until it can find a solution (maximum repeat=k) and save the number of iterations needed to solve this
#(l*100 will then mean that it could not be solved)
k=100
results=[]
for i in range(len(bad_targets)):
    j=0
    succes=0
    iterations=0
    while succes==0 and j<k:
        j+=1
        current_shifted_target = bad_targets[i] + 0.01 * np.random.rand(n)
        temp_sol=newton(np.random.rand(n),current_shifted_target,0.0001,100)
        succes=temp_sol[0]
        iterations += temp_sol[2]
    results.append(iterations)

#Exporting results to a .xlsx file
results_to_excel(results,"results.xlsx")







