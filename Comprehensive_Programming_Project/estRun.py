import numpy as np
import scipy as sp
from scipy import stats
#NO OTHER IMPORTS ALLOWED (However, you're allowed to import e.g. scipy.linalg)

def estRun(dt, internalStateIn, steeringAngle, pedalSpeed, measurement):
    #  The function arguments are: 
    #  dt: current time step [s]
    #  internalStateIn: the estimator internal state
    #  steeringAngle: gamma [rad] 
    #  pedalSpeed: omega [rad/s] 
    #  measurement: the position measurement valid at the current time step
    
    #  Note: the measurement is a 2D vector, of x-y position measurement.

    x = internalStateIn[0]
    y = internalStateIn[1]
    theta = internalStateIn[2]
    r = internalStateIn[3]
    B = internalStateIn[4]
    w_mean = internalStateIn[5]
    w_var = internalStateIn[6]

    N = x.shape[0]

    v_omega = np.random.normal(0, np.pi / 90, size = N)
    v_gamma = np.random.normal(0, np.pi / 36, size = N)
    v_velocity = np.random.normal(0, 1, size = N)

    for n in range(N):
        x[n] = x[n] + (5 * r[n] * (pedalSpeed + v_omega[n]) + v_velocity[n]) * np.cos(theta[n]) * dt
        y[n] = y[n] + (5 * r[n] * (pedalSpeed + v_omega[n]) + v_velocity[n]) * np.sin(theta[n]) * dt
        theta[n] = theta[n] + (5 * r[n] * (pedalSpeed + v_omega[n]) + v_velocity[n]) * np.tan(steeringAngle + v_gamma[n]) * dt / B[n]

    if not (np.isnan(measurement[0])): # have a valid measurement
        fzx = stats.norm.pdf(measurement[0] - x - B * np.cos(theta) / 2, 
        w_mean[0], w_var[0, 0]) * stats.norm.pdf(measurement[1] - y - B * np.sin(theta) / 2, w_mean[1], w_var[1, 1])
        beta = (1 / np.sum(fzx)) * fzx

        # Resampling
        rho = np.random.uniform(0, 1, size = N)
        cumsum = np.cumsum(beta)
        idx = np.searchsorted(cumsum, rho)
        xm, ym, thetam = x[idx], y[idx], theta[idx]
    
    else:
        xm, ym, thetam = x, y, theta

    x, y, theta = np.mean(xm), np.mean(ym), np.mean(thetam)


    # Update the internal state
    internalStateOut = [xm,
                     ym,
                     thetam, 
                     r, 
                     B, 
                     w_mean, 
                     w_var
                     ]

    #  The function has four outputs:
    #  x: the current best estimate for the bicycle's x-position
    #  y: the current best estimate for the bicycle's y-position
    #  theta: the current best estimate for the bicycle's heading angle
    #  internalStateOut: the estimator's internal state, in a format that can be understood by the next call to this function
    return x, y, theta, internalStateOut 


