class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        lengths = ""

        if not strs:
            return res

        for s in strs:
            l = len(s)
            lengths += "," + str(l)
            res += "#" + s

        return lengths[1:] + res

    def decode(self, s: str) -> List[str]:
        res = []
        lengths = []

        if not s:
            return res

        print(s)

        i = 0
        while i < len(s) and s[i] != "#":
            length = ""
            while i < len(s) and s[i] != "," and s[i] != "#":
                length += s[i]
                i += 1

            lengths.append(int(length))
            if i < len(s) and s[i] == ',':
                i += 1
        i += 1

        for l in lengths:
            res.append(s[i:i + l])
            i = i + l + 1
        
        return res
                


        
