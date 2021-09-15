def cumulative_sum(self, lst : List[int])  -> List[int]:
        _sum = 0
        res = [_sum := _sum + lst[i] for i in range(0, len(lst))]
        return res
