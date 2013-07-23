import math
from udacityplots import *
import matplotlib.pyplot

moon_distance = 384e6 # m

def orbit():
    num_steps = 50
    x = numpy.zeros([num_steps + 1, 2])
    
    theta = 2*math.pi/num_steps

    for step in range(num_steps + 1):
        thetaStep = theta * step
        x[step, 0] = moon_distance*math.cos(thetaStep)
        x[step, 1] = moon_distance*math.sin(thetaStep)
    return x

x = orbit()
print len(x)

@show_plot
def plot_me():
    matplotlib.pyplot.axis('equal')
    matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
plot_me()