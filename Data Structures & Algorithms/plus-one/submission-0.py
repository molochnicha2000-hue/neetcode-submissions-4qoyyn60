class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = []
        for i in digits:
            num.append(str(i))
        
        number = int("".join(num))
        number += 1
        number = str(number)
        res = []
        for i in number:
            res.append(int(i))
        return res
        