def Subarray(self, arr : List[int]) -> int:
        res = []
        for i in range(len(arr)):
            for j in range(i):
                res.append(arr[j:i])
        return res
