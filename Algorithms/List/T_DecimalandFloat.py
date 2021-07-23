# Applying Discounts
class Solution:
    def get_discounts(self, lst : list, d : str) -> list:
        d = int(d.strip('%'))
        res = []
        for i in lst:
            dis = 0
            dis = (i * d) / 100
            res.append(str(dis))
        result = []
        for i in res:
            if '.0' in i:
                result.append(int(i[:-2]))
            else:
                result.append(float(i))
        return result
