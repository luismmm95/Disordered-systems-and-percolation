import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

def plot(X, Y, titl='', Xlabel='X axis', Ylabel='Y axis', ltype = 'o--'):
    
    fig, ax = plt.subplots(figsize=(14, 7))
    if type(Y) is list:
        if type(X) is list:
            for i in range(0,len(Y)):
                ax.plot(X[i].T,Y[i].T,ltype)
        else:
            for i in range(0,len(Y)):
                ax.plot(X.T,Y[i].T,ltype)
    else:
        ax.plot(X,Y,ltype)
        
    ax.set_xlabel(Xlabel)
    ax.set_ylabel(Ylabel)
    ax.set_title(titl)
    plt.grid()
    
    SMALL_SIZE = 12
    MEDIUM_SIZE = 14
    BIGGER_SIZE = 16

    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    
    return fig, ax

def contour(Z, X=[], Y=[], titl='Contour plot', Xlabel='X axis', Ylabel='Y axis'):    
    
    if X == [] and Y == []:
        M,N = Z.shape
        ax_rows = np.linspace(0,1,M)
        ax_cols = np.linspace(0,1,N)

        [X,Y] = np.meshgrid(ax_rows, ax_cols)
    else:
        [X,Y] = np.meshgrid(X, Y)

    fig, ax = plt.subplots(figsize=(10,10))
    ax.contourf(X, Y, Z, cmap=cm.PuRu_r)
    
    ax.set_xlabel(Xlabel)
    ax.set_ylabel(Ylabel)
    ax.set_title(titl)
    
    SMALL_SIZE = 12
    MEDIUM_SIZE = 14
    BIGGER_SIZE = 16

    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ztick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    
    plt.show()

def surface_plot(Z, X=[], Y=[], titl='Surface plot', Xlabel='X axis', Ylabel='Y axis', Zlabel='Z axis'):    
    
    if X == [] and Y == []:
        M,N = surface.shape
        ax_rows = linspace(0,1,M)
        ax_cols = linspace(0,1,N)

        [X,Y] = np.meshgrid(ax_rows, ax_cols)
    else:
        [X,Y] = np.meshgrid(X, Y)

    fig = plt.figure(figsize=(14,7))
    ax = fig.gca(projection='3d')
    ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0)
    ax.set_xlabel(Xlabel)
    ax.set_ylabel(Ylabel)
    ax.set_zlabel(Zlabel)
    ax.set_title(titl)
    
    SMALL_SIZE = 12
    MEDIUM_SIZE = 14
    BIGGER_SIZE = 16

    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ztick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    
    plt.show()
    
def contour3d_plot(Z, X=[], Y=[], titl='3D contour plot', Xlabel='X axis', Ylabel='Y axis', Zlabel='Z axis'):
    xmin = np.amin(X)
    ymax = np.amax(Y)
    zmin = np.amin(Z)
    
    if X == [] and Y == []:
        M,N = surface.shape
        ax_rows = linspace(0,1,M)
        ax_cols = linspace(0,1,N)

        [X,Y] = np.meshgrid(ax_rows, ax_cols)
    else:
        [X,Y] = np.meshgrid(X, Y)
    
    fig = plt.figure(figsize=(14,7))
    ax = fig.gca(projection='3d')
    ax.plot_surface(X, Y, Z, alpha=0.3)
    cset = ax.contourf(X, Y, Z, zdir='z', offset=zmin, cmap=cm.coolwarm)
    cset = ax.contourf(X, Y, Z, zdir='x', offset=xmin, cmap=cm.coolwarm)
    cset = ax.contourf(X, Y, Z, zdir='y', offset=ymax, cmap=cm.coolwarm)

    ax.set_xlabel(Xlabel)
    ax.set_ylabel(Ylabel)
    ax.set_zlabel(Zlabel)
    ax.set_title(titl)
    
    SMALL_SIZE = 12
    MEDIUM_SIZE = 14
    BIGGER_SIZE = 16

    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ztick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    
    plt.show()