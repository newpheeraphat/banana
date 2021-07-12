def hamming_distance(txt1, txt2):
	diff = 0 
	for i, j in zip(txt1, txt2):
		if i != j:
			diff += 1
	return diff
