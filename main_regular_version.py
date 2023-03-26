from equations_groebner_tester import *
from multiprocessing import Pool
import time

if __name__ == '__main__':
    # List of Parameters
    parameters = [i for i in range(3, 9)]

    #Groebner basis computations
    start = time.perf_counter()
    for i in parameters:
        tester_faster(i)
    finish = time.perf_counter()

    time=str(round(finish - start, 2))

    log_file = open("time_regular.txt", "w")
    log_file.write(time)
    log_file.close()
