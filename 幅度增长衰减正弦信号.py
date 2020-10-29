import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math

N = 500
t = np.linspace(-5.0,5.0,1000)
plt.ylim(-10,10)
# w = pi
fs = 1.0
x1 =  np.cos(2 * math.pi * fs * t)*np.exp(0.3*t) 
plt.subplot(221)
plt.plot(t,x1)
plt.xlabel("x")
plt.ylabel("y")
x2 =  np.cos(2 * math.pi * fs * t)*np.exp(0.3*-t) 
plt.subplot(222)
plt.plot(t,x2)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
