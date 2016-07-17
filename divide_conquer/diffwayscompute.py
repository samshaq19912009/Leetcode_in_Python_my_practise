"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
Input: "2-1-1"
((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0,2]


Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

Output: [-34, -14, -10, -10, 10]
"""


class Solution:
    def differwaysCompute(self, input):
        return [eval('a'+c+'b')
                for i, c in enumerate(input) if c in "+-*"
                for a in self.differwaysCompute(input[:i])
                for b in self.differwaysCompute(input[i+1:])] or [int(input)]

