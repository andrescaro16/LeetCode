# Time complexity: O(n log n)
# Space complexity: O(n)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        answer = ""
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                answer += strs[0][i]
            else:
                break

        return answer

