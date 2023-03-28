from equations_groebner_tester import *
import time

if __name__ == '__main__':
    # List of Parameters
    parameters = [i for i in range(2, 9)]

    #Groebner basis computations
    start = time.perf_counter()
    for i in parameters:
        tester_F5_simpler_system(i)
    finish = time.perf_counter()

    time=str(round(finish - start, 2))

    log_file = open("time_regular_tester_F5_simpler_system.txt", "w")
    log_file.write(time)
    log_file.close()
