class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        dic = {}
        used = set()
        words = s.split()
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            letter = pattern[i]
            word = words[i]
            if letter in dic:
                if dic[letter] != word:
                    return False
            else:
                if word in used:
                    return False

            
                dic[letter] = word
                used.add(word)
        return True

        