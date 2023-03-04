from Equation import Expression
from math import pi
import re

# Tests if the user entered something like "2x+5" which isn't parsed. Nothing stops him to write "xy" instead of "x*y" though.

expr = "sin(5x+4)"

if re.search("[0-9]+[a-zA-Z]+[0-9]*", expr) != None :
	print("Multiplication should be explicit : \"3*y\" instead of \"3y\"")


# Super simple example of how the parser works. No need to import sin, it works as is. But we could check the precision of the sin function imported.

expr = "sin(5*x+4)"

f = Expression(expr)

print([f(x/10*2*pi) for x in range(10)])
