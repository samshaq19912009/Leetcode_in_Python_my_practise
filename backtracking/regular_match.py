"""
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

"""

class Solution(object):
    #recursive
    #TLE
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        
        if len(p) == 1 or p[1] != '*':
            if len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        else:
            while len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                if self.isMatch(s, p[2:]):
                    return True
                s = s[1:]
            return self.isMatch(s, p[2:])
        
    def isMatch(self, s, p):
        dp = [[False for j in xrange(len(p)+1)] for i in xrange(len(s)+1)]
        
        dp[0][0] = True
        for j in xrange(2, len(p)+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
                
        for i in xrange(1, len(s)+1):
            for j in xrange(1, len(p)+1):
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
                else:
                    dp[i][j] = dp[i][j-2] or  (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))

        return dp[len(s)][len(p)]

