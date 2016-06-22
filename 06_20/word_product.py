class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)

        if n == 0:
            return 0

        element = [0] * n

        for i, s in enumerate(words):
            for c in s:
                element[i] |= 1 << (ord(c) - 97)

        ans = 0
        for i in range(n-1):
            for j in range(i, n):
                if element[i] & element[j] == 0:
                    ans = max(ans, len(words[i])*len(words[j]))

        return ans
            
