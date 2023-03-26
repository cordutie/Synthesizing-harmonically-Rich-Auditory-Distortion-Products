from equations_groebner_tester import *
from multiprocessing import Pool
import time

if __name__ == '__main__':
    # List of Parameters
    parameters = [i for i in range(1, 9)]

    # Multiprocessing
    start = time.perf_counter()
    with Pool(processes=None) as p:
        results = p.map(tester, parameters)
    finish = time.perf_counter()

    time=round(finish - start, 2)

    log_file = open("time_multiprocessing.txt", "w")
    log_file.write(time)
    log_file.close()