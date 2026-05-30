class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        lengths = []

        if strs == []:
            return ""

        for s in strs:
            lengths.append(str(len(s)))
            res.append(s)

        return ",".join(lengths) + "#" + "#".join(res)

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
                


        
