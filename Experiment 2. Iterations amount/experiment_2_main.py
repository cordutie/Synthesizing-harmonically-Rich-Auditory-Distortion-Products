from Preamble.functions import *

#Create a list of m targets of n entries
m=1000
n=16
targets=[]
for i in range(m):
    targets.append(np.random.rand(n))

#Try to solve every target up to l times and save the targets that could be solved in less than 10 tries with 100 iterations each
l=10
good_targets=[]
for i in range(len(targets)):
    j=0
    succes=0
    while succes==0 and j<l:
        j+=1
        temp_sol=newton(np.random.rand(n),targets[i],0.0001,100)
        succes=temp_sol[0]
    if succes==1:
        good_targets.append(targets[i])

print(str(len(good_targets))+" good targets were found.")

#Now we solve the problem for each good target coounting their iterations using tolerance = 20
size=len(good_targets)
results=np.empty(size)
for i in range(len(good_targets)):
    succes=0
    iterations=0
    while succes==0:
        temp_sol=newton(np.random.rand(n),good_targets[i],0.0001,20)
        succes=temp_sol[0]
        iterations+= temp_sol[2]
    results[i]=iterations

print("Using tolerance = 20:")
print("mean          = "+str(np.mean(results)))
print("percentile 90 = "+str(np.percentile(results,90)))
print("percentile 99 = "+str(np.percentile(results,99)))


#Now we solve the problem for each good target coounting their iterations using tolerance = 30
size=len(good_targets)
results=np.empty(size)
for i in range(len(good_targets)):
    succes=0
    iterations=0
    while succes==0:
        temp_sol=newton(np.random.rand(n),good_targets[i],0.0001,30)
        succes=temp_sol[0]
        iterations+= temp_sol[2]
    results[i]=iterations

print("Using tolerance = 30:")
print("mean          = "+str(np.mean(results)))
print("percentile 90 = "+str(np.percentile(results,90)))
print("percentile 99 = "+str(np.percentile(results,99)))


#Now we solve the problem for each good target coounting their iterations using tolerance = 40
size=len(good_targets)
results=np.empty(size)
for i in range(len(good_targets)):
    succes=0
    iterations=0
    while succes==0:
        temp_sol=newton(np.random.rand(n),good_targets[i],0.0001,40)
        succes=temp_sol[0]
        iterations+= temp_sol[2]
    results[i]=iterations

print("Using tolerance = 40:")
print("mean          = "+str(np.mean(results)))
print("percentile 90 = "+str(np.percentile(results,90)))
print("percentile 99 = "+str(np.percentile(results,99)))


#Now we solve the problem for each good target coounting their iterations using tolerance = 50
size=len(good_targets)
results=np.empty(size)
for i in range(len(good_targets)):
    succes=0
    iterations=0
    while succes==0:
        temp_sol=newton(np.random.rand(n),good_targets[i],0.0001,50)
        succes=temp_sol[0]
        iterations+= temp_sol[2]
    results[i]=iterations

print("Using tolerance = 50:")
print("mean          = "+str(np.mean(results)))
print("percentile 90 = "+str(np.percentile(results,90)))
print("percentile 99 = "+str(np.percentile(results,99)))

