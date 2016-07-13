"""
Get the hints from guess

"""


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        sdict = collections.defaultdict(int)
        gdict = collections.defaultdict(int)
        for s in secret:
            sdict[s] += 1
        for g in guess:
            gdict[g] += 1
        total = 0
        for value in sdict.keys():
            if value in gdict.keys():
                total += min(sdict[value], gdict[value])
        bull = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
        
        ans = str(bull) + 'A' + str(total-bull) + 'B'
        
        return ans
            
