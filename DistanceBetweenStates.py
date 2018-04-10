import numpy as np
import matplotlib.pyplot as plt

# this does not work now

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

distance_between_states = [j - i for i, j in zip(array[:-1], array[1:])]

x = np.arange(len(distance_between_states))
plt.scatter(x, distance_between_states)
plt.ylabel("Distance Between States")
plt.xlabel("States")
plt.show()
