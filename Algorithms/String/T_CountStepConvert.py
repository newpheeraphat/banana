def steps_to_convert(txt):
	isupper = [x for x in txt if x.isupper()]
	islower = [x for x in txt if x.islower()]
	return min(len(isupper), len(islower))
