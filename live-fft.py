from time import sleep

from parsetools import *
from ffttools import *
from plottools import *

fig, data = prepareInteractivePlot()

setWindow([0,20000], [0,1])

context = fftsetup()

for i in range(150) :

	try :
		f = stringToFunc(input("Expression du signal : "))

		xf, yf = ft(context, f)

		replaceData(data, xf, yf)
		adaptWindow(data)

		fig.canvas.draw()
		fig.canvas.flush_events()

		sleep(0.05)

	except Exception as e :
		print(e)