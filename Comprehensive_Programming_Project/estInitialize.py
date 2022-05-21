import numpy as np
import scipy as sp
#NO OTHER IMPORTS ALLOWED (However, you're allowed to import e.g. scipy.linalg)

def estInitialize():
    # Fill in whatever initialization you'd like here. This function generates
    # the internal state of the estimator at time 0. You may do whatever you
    # like here, but you must return something that is in the format as may be
    # used by your estRun() function as the first returned variable.
    #
    # The second returned variable must be a list of student names.
    # 
    # The third return variable must be a string with the estimator type

    #we make the internal state a list, with the first three elements the position
    # x, y; the angle theta; and our favorite color. 
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

    # note that there is *absolutely no prescribed format* for this internal state.
    # You can put in it whatever you like. Probably, you'll want to keep the position
    # and angle, and probably you'll remove the color.
    internalState = [x,
                     y,
                     theta, 
                     r, 
                     B,
                     w_mean,
                     w_var
                     ]

    # replace these names with yours. Delete the second name if you are working alone.
    studentNames = ['Pu Wang',
                    'Ning Zhang']
    
    # replace this with the estimator type. Use one of the following options:
    #  'EKF' for Extended Kalman Filter
    #  'UKF' for Unscented Kalman Filter
    #  'PF' for Particle Filter
    #  'OTHER: XXX' if you're using something else, in which case please
    #                 replace "XXX" with a (very short) description
    estimatorType = 'PF'
    
    return internalState, studentNames, estimatorType