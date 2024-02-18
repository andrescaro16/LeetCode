class Solution:
    
    # Time complexity: O(n)
    # Space complexity: O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        
        readT = {}
        readS = {}

        for i in range(max(len(t), len(s))):
            if i < len(t):
                if readT.get(t[i]) is None:
                    readT[t[i]] = 1
                else:
                    readT[t[i]] += 1
            if i < len(s):
                if readS.get(s[i]) is None:
                    readS[s[i]] = 1
                else:
                    readS[s[i]] += 1

        if readT == readS:
            return True
        
        return False
