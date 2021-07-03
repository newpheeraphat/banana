def count_char(txt):
   set1 = set(txt)
   dict1 = {}
   for s in set1:
      count_ele = txt.count(s)
      dict1[s] = count_ele
   get_values = dict1.values()
   return sum(get_values)/2
