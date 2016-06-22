class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()

        if len(pattern) != len(words):
            return False

        paDict, wordDict = {}, {}

        for pa, word in zip(pattern, words):
            if pa not in paDict:
                paDict[pa] = word
            if word not in wordDict:
                wordDict[word] = pa

            if wordDict[word] != pa or paDict[pa] != word:
                return False

        return True
