import matplotlib.pyplot as plt
import numpy as np
import time

title = "Redmar <3 Gabriela"

x = np.arange(0, 10)
y = np.arange(0, 10)

fig, ax = plt.subplots()

ax.scatter(-x,-y)
plt.show()

time.sleep(1)

update = True

if update:
    ax.clear()
    plt.title(title)

else:
    plt.close()
    fig = plt.figure()
    ax = fig.add_subplot()
    plt.title(title)
    plt.tight_layout()

ax.set_xlabel('x (nm)')
ax.set_ylabel('y (nm)')

ax.scatter(x, y)

plt.draw()

plt.pause(0.05)

time.sleep(1)

