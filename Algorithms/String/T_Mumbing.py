def mumbling(s):
	my_list = []
	for count, i in enumerate(s, 1):
		my_list.append(count * i)
	res = [i.capitalize() for i in my_list]
	return "-".join(res)

# "M-Uu-Bbb-Aaaa-Sssss-Hhhhhh-Iiiiiii-Rrrrrrrr"
