import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

def plot_pdf(mean, cov, samples):
    distr = multivariate_normal(cov=cov, mean=mean, seed=samples)
    x = np.linspace(-3*cov[0][0], 3*cov[0][0], num=100)
    y = np.linspace(-3*cov[1][1], 3*cov[1][1], num=100)
    X, Y = np.meshgrid(x, y)
    pdf = np.zeros(X.shape)
    
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            pdf[i, j] = distr.pdf([X[i, j], Y[i, j]])

    plt.contourf(X, Y, pdf, cmap='viridis')
    E_XY = np.mean(X * Y)
    print("E[XY]:", E_XY)
    V_XY = np.var(X * Y)
    print("VAR[XY]:", V_XY)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, pdf, cmap='viridis')
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.show()

mean = [0, 1]
cov = [[1, 0], [0, 2]]
samples = 200
print("samples:",samples)
plot_pdf(mean, cov, samples)

print("- - - - - - - - - - - - - - - - - - - - - -")

samples = 10
print("samples:",samples)
plot_pdf(mean, cov, samples)

