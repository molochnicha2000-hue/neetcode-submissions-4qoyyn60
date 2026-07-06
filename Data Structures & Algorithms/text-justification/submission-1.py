class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        N = len(words)
        res = []

        current = []
        current_len = 0
        def get(current, current_len):
            extra_space = maxWidth - current_len
            spaces = extra_space // max(len(current) - 1, 1)
            remainder = extra_space % max(len(current) - 1, 1)
       
            for j in range(max(1, len(current) - 1)):
                current[j] += " " * spaces
                if remainder:
                    current[j] += " "
                    remainder -= 1

            return "".join(current)

        for i in range(N):
            if current_len + len(current) + len(words[i]) > maxWidth:
                new = get(current, current_len)
                res.append(new)

                current = []
                current_len = 0
                
            current += [words[i]]
            current_len += len(words[i])

        last = " ".join(current)
        extra_space = maxWidth - (len(last))
        
        last += " " * extra_space
        res.append(last)
        return res






