import numpy as np
import matplotlib.pyplot as plt

a=[]
n=100
for i in range(1000000):
    a.append(np.random.randint(n))

plt.hist(a,n)
plt.show()