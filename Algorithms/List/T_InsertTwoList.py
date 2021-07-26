# Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1 : str, word2 : str) -> str:
        import itertools
        char1 = list(word1)
        char2 = list(word2)
        res = []
        result = []
        total = []
        for combination in itertools.zip_longest(char1, char2, fillvalue="anything"):
            res.append(combination)
        for i, j in res:
            result.append(i)
            result.append(j)
        total = [x for x in result if x != "anything"]
        return res
