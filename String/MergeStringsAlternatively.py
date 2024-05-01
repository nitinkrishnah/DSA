# https://leetcode.com/problems/merge-strings-alternately/

def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ''
        minLen = min(len(word1),len(word2))
        for i in range(minLen):
            s += word1[i]+word2[i]
        s += word1[minLen:] + word2[minLen:]
        return s