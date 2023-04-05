from time import sleep
from threading import Thread

from parsetools import *
from ffttools import *
from plottools import *

def getexpr() :
	global s
	global running

	while running :
		s = input("Expression du signal ('q' pour quitter) : ").strip()

		if s == 'q' :
			running = 0


def plot() :
	global s
	global running

	while running :

		try :
			f = stringToFunc(s)

			xf, yf = ft(context, f)

			replaceData(data, xf, yf)
			adaptWindow(data)

			fig.canvas.draw()
			fig.canvas.flush_events()

		except Exception as e :
			print(e)

		sleep(0.05)

fig, data = prepareInteractivePlot()

setWindow([0,20000], [0,1])

context = fftsetup()

s = ""

gexpr = Thread(target=getexpr)
thplot = Thread(target=plot)

running = 1

gexpr.start()
thplot.start()

gexpr.join()
thplot.join()
