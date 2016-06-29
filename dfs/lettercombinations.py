class Solution:
    def letterCombinations(self, digits):
        if not digits or len(digits) == 0:
            return []
        n = len(digits)
        
        def dfs(num, string, ans):
            if num == n:
                ans.append(string)
                return
            for letter in dict[digits[num]]:
                dfs(num+1, string+letter, ans)
                
        dict = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                }
        
        ans = []
        paht  = ''
        dfs(0, path, ans)
        retrurn ans
