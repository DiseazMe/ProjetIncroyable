import matplotlib.pyplot as plt
import numpy as np

def f(x):
	return x**2

x = np.linspace(0,1,100)
y = f(x)

plt.plot(x,y)
plt.show()
