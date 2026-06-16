class Solution:
    def romanToInt(self, s: str) -> int:
        need = {"I" : 1,
                "V" : 5,
                "X" : 10,
                "L" : 50,
                "C" : 100,
                "D" : 500,
                "M" : 1000
                }

        stack = []
        res = 0
        for char in s:
            if stack and stack[-1] == "I" and char == "V":
                res -= need[stack.pop()]
                res += 4

            elif stack and stack[-1] == "I" and char == "X":
                res -= need[stack.pop()]
                res += 9

            elif stack and stack[-1] == "X" and char == "L":
                res -= need[stack.pop()]
                res += 40
            
            elif stack and stack[-1] == "X" and char == "C":
                res -= need[stack.pop()]
                res += 90 

            elif stack and stack[-1] == "C" and char == "D":
                res -= need[stack.pop()]
                res += 400
            
            elif stack and stack[-1] == "C" and char == "M":
                res -= need[stack.pop()]
                res += 900 
            else:  
                res += need[char]
            stack.append(char)
            

        return res