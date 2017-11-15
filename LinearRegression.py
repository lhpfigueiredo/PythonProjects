"""
Use pyhton 3.6 with numpy and matplotlib
"""

import numpy as np
from matplotlib import pyplot as mp
import random


m = 9
dataset_x = (np.concatenate((np.ones((1,m)), [np.linspace(1,m,m)])).transpose())
dataset_y = (0.3 + np.linspace(1,m,m)*0.2)



def measure(theta0, theta1):
    squaredError = 0
    m = len(dataset_x)
    for i in range(0, m):
        error = (hypothesis(theta0, theta1, dataset_x[i]) - dataset_y[i]) * (hypothesis(theta0, theta1, dataset_x[i]) - dataset_y[i])
        squaredError += error

    return ((1/(2*m))*squaredError)


def hypothesis(theta0, theta1, x):
    return theta0*x[0] + theta1*x[1]


def gradientDescent(theta0, theta1, index):
    partialDerivative = 0
    m = len(dataset_x)
    for i in range(0, m):
        error = (hypothesis(theta0, theta1, dataset_x[i]) - dataset_y[i]) * dataset_x[i][index]
        partialDerivative += error

    return ((1 / (m)) * partialDerivative)


def main():

    theta0 = random.random()
    theta1 = random.random()

    alpha = 0.01

    error0 = 9999999999
    error1 = 9999999999

    iterations = 0
    mp.ion()
    costHistory = []

    while True:
        error0 = error1
        error1 = measure(theta0, theta1)
        costHistory.append(error1)
        #print(error1)

        tempTheta0 = gradientDescent(theta0, theta1, 0)
        tempTheta1 = gradientDescent(theta0, theta1, 1)

        theta0 = theta0 - alpha * tempTheta0
        theta1 = theta1 - alpha * tempTheta1

        iterations += 1

        #if (iterations%1000) == 0:
        #    print(iterations)

        if error0 - error1 < 0.0000000001 and error0 - error1 > 0:
            print("h = " + str(theta0) + "*x0 + " + str(theta1) + "*x1")
            print("It takes: " + str(iterations))
            print("Error: " + str(measure(theta0, theta1)))
            #mp.plot(costHistory)
            break
        if error0 - error1 < 0:
            print("It will diverge!")
            break
    pass

main()