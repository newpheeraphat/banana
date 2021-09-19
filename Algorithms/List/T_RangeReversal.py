def ranged_reversal(lst, start, finish):
	return lst[:start] + lst[start:finish + 1][::-1] + lst[finish+1:]
