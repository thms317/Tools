# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 17:51:16 2018

@author: noort
"""

import matplotlib as mpl

mpl.use(u'TkAgg')
mpl.interactive(True)

import numpy as np
import matplotlib.pyplot as plt
import MTfiberWLC as MT
from lmfit import Minimizer, Parameters, report_fit
from mpl_toolkits.mplot3d import Axes3D


def partext(selected=''):
    global pars
    text = ''
    for par in pars.valuesdict():
        if (par == selected):
            text += '> '
        else:
            text += '  '
        text += str(par).ljust(12)
        text += "{:6.2f}".format(pars.valuesdict()[par])

        if pars[par].vary:
            text += u' \xb1'
        text += '\n'
    #        if par == 'tmax_s':
    #            text +='\n'
    return text


def old_init_parplot(pars, D3=False):
    global plt
    global txt


def keyevent(event=None):
    global selected
    global buf
    global plt
    global txt
    if event == None:
        return

    print('Event!!!!', event.key)

    print(event.key)
    try:
        buf += event.key
    except:
        buf = event.key
    try:
        pars[selected].value = float(buf)
    except:
        if buf != '-':
            buf = ''
    try:
        selected = selected
    except:
        selected = pars.valuesdict().keys()[0]

    key = event.key.split('+')
    i = pars.valuesdict().keys().index(selected)
    if key[-1] == u'down':
        i += 1
        if i >= len(pars): i = 0
        selected = pars.valuesdict().keys()[i]
    elif key[-1] == u'up':
        i -= 1
        if i < 0: i = len(pars) - 1
        selected = pars.valuesdict().keys()[i]
    elif key[-1] in [u'left', u'right']:
        if pars[selected].value == 0:
            step = 0
        else:
            step = np.floor(np.log10(np.abs(pars[selected].value))) - 1
        if (step < -1): step = -1
        multiplier = 1
        if key[0] == u'alt': step += 1
        if key[0] == u'ctrl': step -= 1
        if key[-1] == u'left': multiplier *= -1
        step = multiplier * 10 ** step
        pars[selected].value += step

    elif event.key == 'ctrl+t':
        pars[selected].vary = not pars[selected].vary
    elif event.key == 'ctrl+x':
        plt.close()
    elif event.key == 'ctrl+a':
        plt.autoscale()
    txt.set_text(partext(selected=selected))
    plot_par_function(pars)
    plt.show()
    return


def handle_close(evt=None):
    global pars
    print('Closed Figure!')
    print(report_fit(pars))
    return


def init_parplot(x, y, fitfunction, pars_in, z=[], w=None, ref=[]):
    import matplotlib.pyplot as plt
    from matplotlib import gridspec

    global plt, txt
    global fit, fittedfunction, pars
    global xval, yval, ref_of

    xval = x
    yval = y
    ref_of = ref
    pars = pars_in

    fittedfunction = fitfunction

    plt.close()
    gridsize = 6
    fig = plt.figure()
    gs = gridspec.GridSpec(gridsize, gridsize)
    #    gs.update(wspace=0.4, hspace=0.4)

    ax1 = fig.add_subplot(gs[:, 0])
    ax1.axis('off')
    txt = ax1.text(-0.9, 0, partext(), fontsize=8, fontdict={'family': 'monospace'})

    if fitfunction.func_name.find('3D'):
        print fitfunction.func_name
        ax2 = fig.add_subplot(111, projection='3d')
        ax2.scatter(x, y, z, s=15, c='b', alpha=0.25)

        x, y, z = fitfunction(x, y, pars, ref=ref_of)
        fit = ax2.plot(x, y, z, color='k', label='3D')
        plt.show()
    else:
        ax2 = fig.add_subplot(gs[:, 2:])
        ax2.scatter(x, y, s=40, facecolors='none', edgecolors='b')
        fit = ax2.plot(x, fitfunction(x, pars), color='k', label='2D')
    fig.canvas.mpl_connect('key_press_event', keyevent)
    fig.canvas.mpl_connect('close_event', handle_close)
    # keyevent()
    # handle_close()
    # plt.show()
    return fig, ax1


def plot_par_function(pars):
    global fit, fittedfunction
    global xval, yval, ref_of

    if str(fit).find('Line2D') > 0:
        fit[0].set_ydata(fittedfunction(xval, pars))
    elif str(fit).find('Line3D') > 0:
        x, y, z = fittedfunction(xval, yval, pars, ref=ref_of)
        fit[0].set_data([x, y])
        fit[0].set_3d_properties(z, 'z')
    plt.show()
    return


def myfunction2D(x, pars):
    y = x * pars.valuesdict()['L_bp']
    return np.sqrt(y)


def myfunction3D(x, y, pars, ref=[]):
    z = x * pars.valuesdict()['P_nm']
    return x, y, z


def main():
    pars = MT.default_pars()
    x = np.arange(10)
    y = x
    x, y, z = myfunction3D(x, y, pars)

    # fig, ax = init_parplot(x, y, myfunction2D, pars)
    fig, ax = init_parplot(x, y, myfunction3D, pars, z=z, ref=[])

    # plt.rcParams['keymap.fullscreen'] = [u'ctrl+f']
    # print plt.rcParams

    # print changepar(144.224, 'up')
    return


if __name__ == "__main__":
    # execute only if run as a script
    main()
