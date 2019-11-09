import numpy as np
import matplotlib.pyplot as plt

arg = np.linspace(0, 1)

f1 = np.poly1d([1,-1,2])
f2 = np.poly1d([2,-3])
f3 = np.poly1d([1,1,-1])

plt.plot(arg, f3(arg), ls='-', label='function f3')
plt.plot(arg, (f1+f2)(arg), ls='-.', label='f1 and f2 sum')

plt.legend()
plt.show()
