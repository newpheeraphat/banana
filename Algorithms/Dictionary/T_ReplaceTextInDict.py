def keyboard_mistakes(txt):
	di = {"4": "A",  "5": "S",  "0": "O",  "1": "I"}
	for k,v in di.items():
		txt =txt.replace(k, v)
		
	return txt
