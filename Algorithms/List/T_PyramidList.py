def pyramid_lists(n):
	result = []
	for i in range(1,n +1):
		result.append([i] * i)
	return result
	
