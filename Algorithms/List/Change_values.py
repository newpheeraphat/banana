def check_score(s):
	import itertools
  # Transpose 2D to 1D
	res = list(itertools.chain.from_iterable(s))
	for key, i in enumerate(res):
		if i == '#':
			res[key] = 5
		elif i == '!!!':
			res[key] = -5
		elif i == '!!':
			res[key] = -3
		elif i == '!':
			res[key] = -1
		elif i == 'O':
			res[key] = 3
		elif i == 'X':
			res[key] = 1
