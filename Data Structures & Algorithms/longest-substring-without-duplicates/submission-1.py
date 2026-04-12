from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) == 1:
            return 1
        
        res = 0
        l = 0
        curr_list = []
        curr_list = deque(curr_list)
        for r in range(len(s)):
            if s[r] in curr_list:
                while s[r] in curr_list:
                    curr_list.popleft()
                curr_list.append(s[r])
            else:
                curr_list.append(s[r])
                if len(curr_list) > res:
                    res = len(curr_list)
        return res
             
        