

import matplotlib.pyplot as plt

import numpy as np

def h(x) :
    return np.sin(x)


x = np.linspace(0,10,100)

plt.plot(x, h(x), 'r--', label = 'seno')
plt.xlabel("tiempo")
plt.ylabel("posicion")
plt.title("funcion seno")
plt.grid()

plt.show()

