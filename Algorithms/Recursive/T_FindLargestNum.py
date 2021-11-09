def find_highest(lst):
	if len(lst) == 1:
		return lst[0]
	return max(lst[len(lst) - 1], find_highest(lst[:-1]))
