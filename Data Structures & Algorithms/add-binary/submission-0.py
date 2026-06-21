class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        temp = int(a, base = 2) + int(b, base = 2)
        

        return bin(temp)[2:]