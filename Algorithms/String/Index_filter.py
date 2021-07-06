def index_filter(indexes, string):
	res = [string[i] for i in indexes]
	return "".join(res).lower()
# using lambda function
index_filter=lambda i,s:''.join(s[x].lower()for x in i)
