class Solution:

    def encode(self, strs: List[str]) -> str:
        """wc#len_prefix#Hellolenprefix2#World"""
        out = str(len(strs)) + "#"
        for s in strs:
            out += str(len(s)) + "#" + s
        return out

    def decode(self, s: str) -> List[str]:
        res = []
        
        sep_index = s.find("#")
        wc_str = s[:sep_index]
        wc = int(wc_str)
        s = s[sep_index + 1:]

        for i in range(wc):
            sep_index = s.find("#")
            len_prefix = int(s[:sep_index])
            s = s[sep_index + 1:]

            res.append(s[:len_prefix])
            s = s[len_prefix:]
        return res


        




        
