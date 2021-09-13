class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = dict()
        for element in nums:
            if element not in freq:
                freq[element] = 1
            else:
                freq[element] += 1
        sorted_freq = sorted(freq.items(), key = lambda kv: kv[1])
        arr = []
        for i, j in sorted_freq:
            if j == 1:
                arr.append(i)
        arr.sort()
        return arr
