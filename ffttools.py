import numpy as np
from scipy.fft import fft, fftfreq

def fftsetup() :
	# Number of sample points
	N = 20000
	# sample spacing
	T = 1.0 / 40000.0
	x = np.linspace(0.0, N*T, N, endpoint=False)
	return {"samples":N, "spacing":T, "absciss":x}

def ft(fftContext, function) :
	x = fftContext["absciss"]
	y = function(x)
	yf = fft(y)
	xf = fftfreq(fftContext["samples"], fftContext["spacing"])
	xf = xf[:fftContext["samples"]//2]
	yf = (2.0/fftContext["samples"] * np.abs(yf))[:fftContext["samples"]//2]
	return xf, yf