import numpy as np
import matplotlib.pyplot as plt

P = 50  # nm
kT = 4.11  # pN nm
n = 10  # number of proteins
L0 = 3646  # base pairs --> total length
L1 = 30  # base pairs --> wrapped length per dimers

f = np.linspace(0, 30, 1000)

y2 = np.full((len(f)), 1)

plt.rcParams.update({'font.size': 14})

# the black dashed line
plt.plot(f, y2, '--', color="black", linewidth=3)
plt.text(0, 1.1, "y=1")

# the colored lines
for n in range(13):
    n *= 10
    y = np.sqrt((P * kT) / f) * ((n * L1) / L0)
    plt.plot(f, y, label=str(n) + " dimers")

'''
# Helmut's suggestion
y_h = np.sqrt((P * kT) / f) - (30 * 0.34)
plt.plot(f, y_h, 'x', label="Helmut's suggestion (dimers wrap 30 base pairs")
y_h = np.sqrt((P * kT) / f)
plt.plot(f, y_h, 'x', label="Helmut's suggestion (dimers wrap 0 base pairs)")
'''

# place plot in second screen
mngr = plt.get_current_fig_manager()
mngr.window.setGeometry(0, -1024, 1920, 984)

plt.ylim(-1, 8)
plt.legend(loc=1)
plt.xlabel("Force (pN)")
plt.ylabel("Length (nm)")
plt.show()
