from equations_groebner_tester import *
from multiprocessing import Pool
import time

if __name__ == '__main__':
    #List of Parameters
    parameters = [i for i in range(2, 7)]

    # #Multiprocessing tester_buch_normal_system
    # start = time.perf_counter()
    # with Pool(processes=None) as p:
    #     results = p.map(tester_buch_normal_system, parameters)
    # finish = time.perf_counter()
    #
    # print("tester_buch_normal_system=" + str(round(finish - start, 5)))

    #Multiprocessing tester_buch_simpler_system
    start = time.perf_counter()
    with Pool(processes=None) as p:
        results = p.map(tester_buch_simpler_system, parameters)
    finish = time.perf_counter()

    print("tester_buch_simpler_system=" + str(round(finish - start, 5)))

    # #Multiprocessing tester_F5_homo_system
    # start = time.perf_counter()
    # with Pool(processes=None) as p:
    #     results = p.map(tester_F5_homo_system, parameters)
    # finish = time.perf_counter()
    #
    # print("tester_F5_homo_system=" + str(round(finish - start, 5)))

    #Multiprocessing tester_F5_simpler_system
    start = time.perf_counter()
    with Pool(processes=None) as p:
        results = p.map(tester_F5_simpler_system, parameters)
    finish = time.perf_counter()

    print("tester_F5_simpler_system=" + str(round(finish - start, 5)))

