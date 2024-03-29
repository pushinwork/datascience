import numpy as np
import random
import pylab
from plot import Generation

global x, y, N, t, p
t = np.loadtxt('t.txt')
N = len(t)
x = np.vstack((t, np.ones(N)))
p = np.loadtxt('p.txt')
y = p

def compute_cost_batch(x, y, theta):
    hx = np.dot(theta.T, x)
    return np.sum(np.array(hx - y) ** 2) /  x.shape[1]

def gradient_descent_batch(alpha, x, y, num_iters):
    m = x.shape[1]
    costs = np.zeros(num_iters)
    for i in range(num_iters):
        hx = np.dot(theta.T, x)
        diff = hx - y
        for j in range(theta.shape[0]):
            theta[j] = theta[j] - (alpha / m) * np.sum(np.dot(diff, x[j, :].T))
        costs[i] = compute_cost_batch(x, y, theta)
        print "iter batch %s | J_batch: %.3f" % (i, costs[i])
    return theta, costs

if __name__ == '__main__':

    theta = np.zeros((2, 1))
    iterations = 60000
    alpha = 0.01
    cost = compute_cost_batch(x, y, theta)
    print "cout initial gradient batch=", cost
    print "point de depart=", theta.T
    theta,costs = gradient_descent_batch(alpha, x, y, iterations)
    print "theta descente gradient batch",theta.T
    # plot regression linaire

    print "Generation d'un graphe de gradient batch..."
    plot1 = Generation()
    plot1.plotData(t, p)
    plot1.plotCurveNamed(t.T, np.dot(x.T,theta), "descente gradient batch")
    plot1.setLabel("x = temps", "y = position")
    plot1.show()
    #plot iterations et couts batch
    pylab.plot(range(iterations), costs)
    pylab.xlabel("#-iterations gradient batch")
    pylab.ylabel("Couts gradient batch")
    pylab.show()
