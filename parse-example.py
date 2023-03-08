from math import pi
from Equation import Expression
from parsetools import *

expr = "sin(54x+4)"

implied = hasImpliedMultiplication(expr)
if implied :
	impliedMultiplicationError(implied)

# Super simple example of how the parser works. No need to import sin, it works as is. But we could check the precision of the sin function imported.

expr = "sin(5*x+4)"
expr = "ln(y)+sqrt(x)"

f = Expression(expr)

print(f)

print([f(x/10*2*pi) for x in range(10)])
