# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        
        rsnDict = {}
        mgzDict = {}
        for i in range(max(len(ransomNote), len(magazine))):
            if i < len(ransomNote):
                if rsnDict.get(ransomNote[i]) is None:
                    rsnDict[ransomNote[i]] = 1
                else:
                    rsnDict[ransomNote[i]] += 1
            if i < len(magazine):
                if mgzDict.get(magazine[i]) is None:
                    mgzDict[magazine[i]] = 1
                else:
                    mgzDict[magazine[i]] += 1
        
        for letter in rsnDict:
            if ((letter not in mgzDict) or (rsnDict[letter] > mgzDict[letter])):
                return False
        
        return True
