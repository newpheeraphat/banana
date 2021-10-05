def filter_unique(self, lst):
  res = [i for i in lst if len(set(i)) == len(i)] 
  return res
