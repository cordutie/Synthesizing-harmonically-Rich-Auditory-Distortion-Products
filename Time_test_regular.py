from equations_groebner_tester import *
import time

#List of Parameters
parameters = [i for i in range(2, 7)]

# #tester_buch_normal_system
# start = time.perf_counter()
# for i in parameters:
#     tester_buch_normal_system(i)
# finish = time.perf_counter()
#
# print("tester_buch_normal_system="+str(round(finish - start, 5)))

#tester_buch_simpler_system
start = time.perf_counter()
for i in parameters:
    tester_buch_simpler_system(i)
finish = time.perf_counter()

print("tester_buch_simpler_system="+str(round(finish - start, 5)))

# #tester_F5_homo_system
# start = time.perf_counter()
# for i in parameters:
#     tester_F5_homo_system(i)
# finish = time.perf_counter()
#
# print("tester_F5_homo_system="+str(round(finish - start, 5)))

#tester_F5_simpler_system
start = time.perf_counter()
for i in parameters:
    tester_F5_simpler_system(i)
finish = time.perf_counter()

print("tester_F5_simpler_system="+str(round(finish - start, 5)))