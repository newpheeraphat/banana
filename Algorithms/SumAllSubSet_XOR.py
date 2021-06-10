# Sum of All Subset XOR Totals
 def subsetXORSum(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bits = 0 
        for i in range(len(nums)):
            bits |= nums[i]
        
        ans = bits * pow(2, len(nums)-1)
        return ans
