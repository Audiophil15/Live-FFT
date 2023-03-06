import numpy as np
from numpy import pi, sin, cos, sqrt
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

from time import sleep

def prepareInteractivePlot() :
	plt.ion()
	fig = plt.figure()
	data, = plt.plot([], [], 'g')

	return fig, data

def replaceData(data, xdata, ydata) :
	data.set_xdata(xdata)
	data.set_ydata(ydata)

def appendData(data, xdata, ydata) :
	data.set_xdata(data.get_xdata().extend(xdata))
	data.set_ydata(data.get_ydata().extend(ydata))

def adaptWindow(data) :
	plt.xlim(min(data.get_xdata())-0.2, max(data.get_xdata())+0.2)
	plt.ylim(min(data.get_ydata())-0.2, max(data.get_ydata())+0.2)

fig, data = prepareInteractivePlot()

# Number of sample points
N = 20000
# sample spacing
T = 1.0 / 40000.0
x = np.linspace(0.0, N*T, N, endpoint=False)

plt.xlim([0,1/T/2])
plt.ylim([-0.2,1.2])

for i in range(150) :

	y = 3*sin(i*10 * 2.0*pi*x) + 0.5*sin(100*i * 2.0*pi*x)
	yf = fft(y)
	xf = fftfreq(N, T)

	replaceData(data, xf[:N//2], (2.0/N * np.abs(yf))[:N//2])
	adaptWindow(data)

	fig.canvas.draw()
	fig.canvas.flush_events()

	sleep(0.05)