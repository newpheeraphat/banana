def sortArrayByParity(self, nums):
        even = []
        odd = []
        while len(nums) != 0 :
            if nums[-1] % 2 == 0:
                even.append(nums.pop())
            else:
                odd.append(nums.pop())
        final = even + odd
        return final
