from Runge_Kutta import RungeKutta
from CONST import *
import numpy as np
from time import time


def get_sequances(x1, x2, x3, x4, x5, x6, h, iterations):

    st = time()
    for _ in range(420):
        x1, x2, x3, x4, x5, x6 = RungeKutta(x1, x2, x3, x4, x5, x6, h)
        

    sequance1 = np.zeros(iterations, dtype=np.float64)
    sequance2 = np.zeros(iterations, dtype=np.float64)
    sequance3 = np.zeros(iterations, dtype=np.float64)
    sequance4 = np.zeros(iterations, dtype=np.float64)
    sequance5 = np.zeros(iterations, dtype=np.float64)
    sequance6 = np.zeros(iterations, dtype=np.float64)
    

    for i in range(iterations):
        x1, x2, x3, x4, x5, x6 = RungeKutta(x1, x2, x3, x4, x5, x6, h)
        sequance1[i] = x1
        sequance2[i] = x2
        sequance3[i] = x3
        sequance4[i] = x4
        sequance5[i] = x5
        sequance6[i] = x6

    print("Time to get sequance: ", time() - st)

    return sequance1, sequance2, sequance3, sequance4, sequance5, sequance6
