class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        the_longest = 0

        nums = set(nums)
        count = 0
        for i in range(len(nums)):
            if (nums[i] - 1) not in nums:
                count = 1
                need_char = nums[i] + 1
                while need_char in nums:
                    count +=1
                    need_char +=1

            the_longest = max(the_longest, count)

        return the_longest
        """
        the_longest = 0
        nums = set(nums)
        count = 0
        for n in nums:
            if (n - 1) not in nums:
                count = 1
                need_char = n + 1
                while need_char in nums:
                    count +=1
                    need_char +=1

            the_longest = max(the_longest, count)

        return the_longest