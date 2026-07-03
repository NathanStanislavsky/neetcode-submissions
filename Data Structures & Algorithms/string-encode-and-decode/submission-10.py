class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word

        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            length_string = ""

            while s[i].isdigit():
                length_string += s[i]
                i += 1

            length_int = int(length_string)

            i += 1

            res.append(s[i:i + length_int])

            i = i + length_int
        
        return res

