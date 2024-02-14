class Solution:

    def isPalindrome(self, s: str) -> bool:

        word = ''

        for letter in s:
            if letter.isalnum():
                word += letter.lower()
        
        if word == word[::-1]:
            return True

        return False
