class Solution:
    def canComplete(self, gas, cost):
        total = 0 ##total sum
        sum = 0 ##temp sum
        #start from the zero 
        #once found negative change the starting point
        j = -1
        for i in range(gas):
            total += gas[i] - cost[i]
            sum += gas[i] - cost[i]
            if sum < 0:
                j = i
                sum = 0#reset the temp sum

        if total >= 0:
            return j+1
        else:
            return -1
