	# <QUESTION 1>

	# Given a string, return the boolean True if it ends in "py", and False if not. Ignore Case.

	# <EXAMPLES>

	# endsDev("ilovepy") → True
	# endsDev("welovepy") → True
	# endsDev("welovepyforreal") → False
	# endsDev("pyiscool") → False

	# <HINT>

	# What was the name of the function we have seen which changes the case of a string?  Use your CLI to access the Python documentation and get help(str).
    
from operator import truediv


def endsPy(input):
	length = len(input)
	f2 = input[(length-2):(length)]
	#print(f2.lower())
	if (f2.lower() == "py"):
		# print("True")
		return True
	else:
		return False

