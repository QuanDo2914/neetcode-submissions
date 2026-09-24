class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letterS, letterT = {}, {}

        for char in s:
            letterS[char] = letterS.get(char,0) +1
        for char in t:
            letterT[char] = letterT.get(char,0) +1
        return letterS == letterT

        # for charS, charT in zip(s, t):
        #     letterS[charS] = letterS.get(charS, 0) + 1
        #     letterT[charT] = letterT.get(charT, 0) + 1


        