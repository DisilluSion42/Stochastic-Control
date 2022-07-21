import numpy as np
import scipy as sp

def estInitialize():
    # This function generates the internal state of the estimator at time 0. 

    N = 1000  

    x = np.random.normal(0, 0.5, size = N)
    y = np.random.normal(0, 0.5, size = N)
    theta = np.random.normal(np.pi / 4, np.pi / 36, size = N)
    r = np.random.normal(0.425, 0.05 * 0.425 / 3, size = N)
    B = np.random.normal(0.8, 0.1 * 0.8 / 3, size = N)

    calibrationData = np.genfromtxt ('data/run_000.csv', delimiter=',')

    keepdims = (np.isnan(calibrationData[:, 3]) == False)

    z_mean = np.mean(calibrationData[:, 3 : 5][keepdims], axis = 0)
    z_var = np.var(calibrationData[:, 3 : 5][keepdims], axis = 0)

    w_mean = np.array([0, 0])
    w_var = np.diag(z_var)

    internalState = [x,
                     y,
                     theta, 
                     r, 
                     B,
                     w_mean,
                     w_var
                     ]


    
    return internalState