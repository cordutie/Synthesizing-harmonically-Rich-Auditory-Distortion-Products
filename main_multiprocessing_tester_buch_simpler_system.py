from equations_groebner_tester import *
from multiprocessing import Pool
import time

if __name__ == '__main__':
    # List of Parameters
    parameters = [i for i in range(2, 9)]

    # Multiprocessing
    start = time.perf_counter()
    with Pool(processes=None) as p:
        results = p.map(tester_buch_simpler_system, parameters)
    finish = time.perf_counter()

    time=round(finish - start, 2)

    log_file = open("time_multiprocessing_tester_buch_simpler_system.txt", "w")
    log_file.write(time)
    log_file.close()