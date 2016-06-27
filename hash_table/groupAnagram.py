##Time: nk*log k
#
class Solution:
    def groupAnagram(self, strs):
        ans = []

        dict = collections.defaultdict(list)

        for s in strs:
            dict[str(sorted(s))].append(s)

        for value in dict.values():
            ans.append(sorted(value))

        return ans
