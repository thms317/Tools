import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

# Initialize plot
fig = plt.figure()
ax1 = plt.subplot()
ax1.set_xlim(-5, 5)
ax1.set_ylim(10, 10)

line = ax1.plot([], [], lw=2)

def handle_close(event):
    print('Closed Figure!')

def onclick(event):
    global setpoint
    if event.button != 1:
        print(event.ydata)


# Set event handlers

cid = fig.canvas.mpl_connect('button_press_event', onclick)
fig.canvas.mpl_connect('close_event', handle_close)

# Create normal plot lines.

plotcols = ["black", "red"]
lines = []
for index in range(2):
    lobj = ax1.plot([], [], lw=2, color=plotcols[index])[0]
    lines.append(lobj)

hdur = 100
sr = 10
times = np.linspace(-hdur,0,hdur*sr)

# Support routine for animations
def init():
    for line in lines:
        line.set_data([], [])
    return lines


def animate(i):

    # Update lines
    x2 = [np.random.normal(), np.random.normal()]
    y2 = [np.random.normal(), np.random.normal()]
    xlist = [times, x2, times]
    ylist = [-1, y2, 1]

    for lnum, line in enumerate(lines):
        line.set_data(xlist[lnum], ylist[lnum])  # set data for each line separately.

    return lines
#

# Use built in animation support from matplotlib to handle the updates of the graph
anim = animation.FuncAnimation(fig, animate, init_func=init, interval=(1000 / sr), blit=True)

plt.show()