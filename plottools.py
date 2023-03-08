import matplotlib.pyplot as plt

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

def setWindow(xlims=[], ylims=[]):
	plt.xlim(xlims)
	plt.ylim(ylims)