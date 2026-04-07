class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = [0] * 26
        t_chars = [0] * 26

        for char in s:
            letter_num = ord(char) - 97
            s_chars[letter_num] += 1
        
        for char in t:
            letter_num = ord(char) - 97
            t_chars[letter_num] += 1
        
        return s_chars == t_chars
        


        