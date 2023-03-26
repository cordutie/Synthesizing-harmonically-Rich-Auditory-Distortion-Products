from equations_groebner_tester import *
from multiprocessing import Pool

if __name__ == '__main__':
    # List of Parameters
    parameters = [i for i in range(1, 9)]

    # Multiprocessing
    with Pool(processes=None) as p:
        results = p.map(tester, parameters)