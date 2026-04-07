class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            charTuple = self.getCharTuple(s)
            if charTuple in groups:
                groups[charTuple].append(s)
            else:
                groups[charTuple] = [s]
        return list(groups.values())

    def getCharTuple(self, x):
        chars = [0] * 26
        for char in x:
            letter_num = ord(char) - 97
            chars[letter_num] += 1
        return tuple(chars)
        
        