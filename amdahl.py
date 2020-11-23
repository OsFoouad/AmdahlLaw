import matplotlib.pyplot as plt
import numpy as np

n = 256
# different x scales 
# x = [1, 2, 4, 8, 16, 32, 64, 128, 256]
x = np.array(np.arange(1, 280, 20))

# first case
f = .5
#r = 256
y1 = [1 / (((1 - f) / (np.sqrt(i))) + ((f * i) / (np.sqrt(i) * n))) for i in x]
plt.plot(x, y1, label="f.5")

# second case
f = .9
# r = 32
y2 = [1 / (((1 - f) / (np.sqrt(i))) + ((f * i) / (np.sqrt(i) * n))) for i in x]
plt.plot(x, y2, label='f=.9')

# third case
f = .975
# r = 16
y3 = [1 / (((1 - f) / (np.sqrt(i))) + ((f * i) / (np.sqrt(i) * n))) for i in x]
plt.plot(x, y3, label='f=.975')

plt.title("SpeedUP and rBCE relation")
plt.xlabel("rBCE")
plt.ylabel("Speed ")
plt.legend()
plt.grid(True)
plt.show()
