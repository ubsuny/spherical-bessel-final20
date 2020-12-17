import math
import numpy as np
from scipy.special import jv, jvp
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML
rc('animation', html='html5')

class AnimatedScatter(object):
    """An animated scatter plot using matplotlib.animations.FuncAnimation."""
    def __init__(self, iterations, x1,y1, x2, y2, color,label, xplot, yplot):
        self.iterations=iterations
        self.numpoints = iterations.shape[0]
        self.color=color
        self.label=label
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.i = 0
        self.xplot=xplot
        self.yplot=yplot
        
        self.stream = self.data_stream()

        # Setup the figure and axes...
        self.fig, self.ax = plt.subplots(figsize=(8,4.5))
        #self.ax.set_title("Demonstration of root finding with " + self.label)
        # Then setup FuncAnimation.
        self.ani = animation.FuncAnimation(self.fig, self.update, interval=200,
                                           frames=25,
                                           init_func=self.setup_plot, blit=False)

    #def setup_plot(self):
    #    """Initial drawing of the scatter plot."""
    #    x,y = next(self.stream)
    #    self.plot = self.ax.plot(self.xplot,self.yplot)
    #    self.plot2 = self.ax.plot( self.xplot, np.zeros_like(self.xplot))
    #    self.scat = self.ax.scatter(x, y, c=np.full_like(x,self.color), vmin=0, vmax=10,
    #                                cmap="jet", edgecolor="k")
    #    self.ax.axis([self.x1,self.x2,self.y1,self.y2])
        
    #    return self.scat,

    def data_stream(self):
        while True:
            yield np.array( [self.iterations[self.i:self.i+1,0],self.iterations[self.i:self.i+1,1]] )

    def update(self, i):
       """Update the scatter plot."""
        self.i = i
        data = next(self.stream)        

        # Set x and y data...
        self.scat.set_offsets(data[0:2].T)

        # We need to return the updated artist for FuncAnimation to draw..
        # Note that it expects a sequence of artists, thus the trailing comma.
        return self.scat,