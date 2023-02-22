# TODO : Detect matching bracket/parenthesis
#		Separate according to operators
#		Replace numbers and create variables, then return function and variable number

def parser(string) :
	operators = "+-*/^"
	delims = {")" : "(", "]" : "["}
	delimsOpen = "(["
	delimsClose = ")]"

	depth = []

	operands = []
	buf = ""

	for c in string :
		if c in delims.values() :
			if len(depth) :
				buf += c
			depth.append(c)
		elif c in delims.keys() :
			if not len(depth) :
				raise ValueError("Closing bracket encountered without an opening one")
			if depth[-1] == delims[c] :
				depth.pop()
			if len(depth) :
				buf += c
		elif c in operators and len(depth) == 0 :
			operands.append(buf)
			buf = ""
		else :
			buf += c

	if len(depth) == 0 :
		operands.append(buf)
	else :
		raise ValueError("Missing closing brackets")

	for i in range(len(operands)) :
		for o in operators :
			if o in operands[i] :
				operands[i] = parser(operands[i])

	return operands

def matchBracket(string, index) :
	try :
		notfound = ("", -1)
		if string[index] not in "([" :
			return notfound
		else :
			if string[index] == "(" :
				matching = ")"
			else :
				matching = "]"

			for i in range(index, len(string)) :
				if string[i] == matching :
					return (string[index+1:i], i)
			return notfound
	except :
		IndexError

if __name__ == "__main__" :

	strs = []
	strs.append("hello + world")
	strs.append("(hello + world)")
	strs.append("(hello) + (world)")
	strs.append("(hello")
	strs.append("hello)")
	strs.append(")hello(")
	strs.append("(2x+4)*8")
	strs.append("(2x+4)*(8+1)")
	strs.append("(2x+4)/((8+2)*5)")

	for s in strs :
		try :
			print(parser(s))
		except Exception as e :
			print("Expression entered : {}".format(s))
			print(e)

