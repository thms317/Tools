import matplotlib.pyplot as plt

# define a plot
fig, ax = plt.subplots()

# get current file manager
mngr = plt.get_current_fig_manager()

# plot the graph
plt.show()

# close the graph and get the QTCore PyRect object
geom = mngr.window.geometry()
x, y, dx, dy = geom.getRect()
print(x, y, dx, dy)

# set the new position with the same size
# mngr.window.setGeometry(0, -1024, 1920, 984)


fig, ax = plt.subplots()
mngr = plt.get_current_fig_manager()
mngr.window.setGeometry(0, -1024, 1920, 984)