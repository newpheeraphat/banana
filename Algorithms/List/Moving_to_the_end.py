def move_to_end(lst, ele):
  res = [x for x in lst if x != ele] + [x for x in lst if x == ele]
  return res
