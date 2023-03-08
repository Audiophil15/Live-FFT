from Equation import Expression
import re

# Tests if the user entered something like "2x+5" which isn't parsed. Nothing stops him to write "xy" instead of "x*y" though.
def hasImpliedMultiplication(expression) :
	found = re.search("[0-9]+[a-zA-Z]+", expression)
	return found

def impliedMultiplicationError(foundExpr) :
	print("Multiplication should be explicit : \"%s\" instead of \"%s\""%( re.search("[0-9]+", foundExpr.group()).group()+"*"+re.search("[a-zA-Z]+", foundExpr.group()).group(), foundExpr.group()))

def stringToFunc(string) :
	found = hasImpliedMultiplication(string)
	if found :
		impliedMultiplicationError(found)
		raise ValueError("The string has implied multiplication")
	else :
		return Expression(string, ["x"])
