def arithmetic_operation(n):
	try:
		return eval(n)
	except ZeroDivisionError:
		return -1
