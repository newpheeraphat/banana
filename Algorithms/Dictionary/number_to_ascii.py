class Solution:
    def num_to_dict(self, lst):
        hashmap = {}
        for i in lst:
            hashmap[i] = chr(i)
        res = []
        for key, values in hashmap.items():
            res.append({str(key):values})
        return res
        # return [{str(i): chr(i)} for i in lst]
        

if __name__ == '__main__':
    p1 = Solution()
    print(p1.num_to_dict([118, 117, 120]))
    print(p1.num_to_dict([101, 121, 110, 113, 103]))
