from operator import le
from pyexpat.model import XML_CTYPE_MIXED
import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-10, 10, 100)
y = 3 + x**2
plt.plot(x, y)
# plt.show()

def grad_1(x):
    return 2*x

def grad_descent(grad, x_current, learning_rate, precision, iters_max):
    for i in range(iters_max):
        print(f"The {i} interation x = {x_current}.")
        grad_current = grad(x_current)
        if abs(grad_current) < precision:
            break
        else:
            x_current = x_current - grad_current*learning_rate
    print(f"The min is x = {x_current}")
    return x_current

if __name__ == '__main__':
    grad_descent(grad_1, x_current=5, learning_rate=0.1, precision=0.000001, iters_max=10000)