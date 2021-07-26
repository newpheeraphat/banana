class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        set1 = set(nums)
        hashmap = dict()
        for s in set1:
            count_all = nums.count(s)
            hashmap[s] = count_all
        nums.sort(key = lambda x: (hashmap[x],-x))
        return nums
