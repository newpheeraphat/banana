def find_int(lst):
  res = list(filter(lambda x: type(x)==int, lst))
  return res
