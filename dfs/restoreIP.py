class Solution:
    def restoreIP(self, s):
        result = []
        ip = []
        self.dfs(s, ip, result, 0)
        return result

    def dfs(s, ip, result, start):
        if len(ip) == 4 and start == len(s):
            tmp  = ".".join(ip)
            result.append(tmp)
            return

        if (len(s) - start) > (4 - len(ip))*3:
            return
        if (len(s) - start) < (4 - len(ip)):
            return

        num = 0
        for i in range(start, start+3):
            num = num*[10] + int(s[i])
            
            if num < 0 or num > 255:
                continue
            ip.append(s[start:i+1])
            dfs(s, ip, result, i+1)
            ip.pop()
            if num == 0:
                break
