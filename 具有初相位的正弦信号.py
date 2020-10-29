import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math

N = 500
t = np.linspace(0,12,num=N)

# w = 3pi/2
fs = 0.75
x3 = 5 * np.sin(2 * math.pi * fs * t)
plt.subplot(212)
plt.plot(t,x3)
plt.title(u'3sin(3pi/2)*t')
plt.ylim(-5.0,5.0)
plt.show()