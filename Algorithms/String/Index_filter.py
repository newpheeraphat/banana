def index_filter(indexes, string):
	res = [string[i] for i in indexes]
	return "".join(res).lower()
