class Solution:
    def get_xp(self, d : dict) -> str:
        dict1 = {"Very Easy": 5,
                "Easy":	10,
                "Medium": 20,
                "Hard":	40,
                "Very Hard": 80}
        res = sum([dict1[x] * d[x] for x in dict1])
        return str(res)

if __name__ == '__main__':
    print(Solution().get_xp({"Very Easy" : 89, "Easy" : 77, "Medium" : 30, "Hard" : 4, "Very Hard" : 1}))
    print(Solution().get_xp({"Very Easy" : 254, "Easy" : 32, "Medium" : 65, "Hard" : 51,"Very Hard" : 34}))
    print(Solution().get_xp({"Very Easy" : 11, "Easy" : 0,"Medium" : 2, "Hard" : 0, "Very Hard" : 27}))
